import pygame
x = pygame.init()

# crating window
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My First Game")

# game specific variable
exit_game = False
game_over = False

# creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                print("you just pressed right key")    
            if event.key == pygame.K_7:
                print("you are pressing key 7")        

pygame.quit()
quit()
