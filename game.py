import pygame
import random
import os

pygame.mixer.init()


pygame.init()

# color
white = (255,255,255)
black = (0, 0, 0, 0)
red = (0,255, 0)

# creating window 
screen_width = 900
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background image
bgimg  = pygame.image.load("gamewall.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

welcomeimg = pygame.image.load("welcome.jpg")
welcomeimg = pygame.transform.scale(welcomeimg, (screen_width, screen_height)).convert_alpha()


# game title
pygame.display.set_caption("Snake Game")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
     screen_text = font.render(text, True, color)
     gameWindow.blit(screen_text, [x,y])

def snake_plot(gameWindow, color, snk_list, snake_size ):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
   
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((210,229,233))
        gameWindow.blit(welcomeimg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True  

            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

# gameloop
def gameloop():
    # game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps =60
    velocity_x = 0
    velocity_y = 0
    velocity_init = 5
    food_x  = random.randint(20, screen_width/2)
    food_y  = random.randint(20, screen_height/2)
    score = 0
    snk_list = []
    snk_length = 1  

    # check if hiscore file exist
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = velocity_init
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -velocity_init
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -velocity_init
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = velocity_init
                        velocity_x = 0
                    
                    if event.key == pygame.K_n:
                        score+=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score = score+10
                food_x  = random.randint(20, screen_width/2)
                food_y  = random.randint(20, screen_height/2)
                snk_length+=5
                if score>int(hiscore):
                    hiscore = score
                    



            gameWindow.fill(white) 
            gameWindow.blit(bgimg, (0,0))
            # generating score in window 
            text_screen("Score:" + str(score)+ "  Hiscore:" + str(hiscore), red, 5, 5)
            # generating snake food
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            # generating snake 
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over =True
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
                
               

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            snake_plot(gameWindow, black, snk_list, snake_size)
        pygame.display.update() 
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
