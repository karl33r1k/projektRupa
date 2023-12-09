import pygame
from sys import exit
from math import ceil
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Jooksja")
clock = pygame.time.Clock()

#Background image
background1 = pygame.image.load('pildid/taust/background1.png')
background1 = pygame.transform.scale(background1,(1000,800))
background2 = pygame.image.load('pildid/taust/background2.png')
background2 = pygame.transform.scale(background2,(1000,800))
background3 = pygame.image.load('pildid/taust/background3.png')
background3 = pygame.transform.scale(background3,(1000,800))

bg1_width = background1.get_width()
bg2_width = background2.get_width()
bg3_width = background3.get_width()

#Enemy image
bat_surface = pygame.image.load('pildid/Enemy sprites/bat_fly.png')

#Game variables
scroll = 0


tiles1 = (ceil(SCREEN_WIDTH / bg1_width)) + 1
tiles2 = (ceil(SCREEN_WIDTH / bg2_width)) + 1
tiles3 = (ceil(SCREEN_WIDTH / bg3_width)) + 1
#print(tiles1)
#print(tiles2)
#print(tiles3)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #Parem versioon run = True, sest Errori võimalus väiksem
    
    for i in range(0,tiles1): #Paneb pildid üksteise kõrvale, järgisin tutoriali Coding With Russ "Infinite Scrolling Background"
        screen.blit(background1,(i * bg1_width + scroll,0))
        screen.blit(background2,(i * bg2_width + scroll,0))
        screen.blit(background3,(i * bg3_width + scroll,0))
    #Scroll background
    scroll -= 5
    #Resetib scrolli (muidu saab pilt otsa)
    if abs(scroll) > bg1_width:
        scroll = 0


    #screen.blit(bat_surface,(800,400))


    pygame.display.update()
    clock.tick(FPS)