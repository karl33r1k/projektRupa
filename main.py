import pygame
from sys import exit

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Mäng')

game_paused = False



clock = pygame.time.Clock()


run = True
while run:



    if game_paused == True:
        pass
    else:
        


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True


        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    pygame.display.update()
    clock.tick(60)
    