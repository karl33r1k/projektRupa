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

#Font
font = pygame.font.Font('Retro Gaming.ttf',50)
#Skoor
skoor_surface = font.render("Minu mäng",False,(64,64,64,))
skoor_rect = skoor_surface.get_rect(center = (400,50))

#Maapind
surface = pygame.image.load('pildid/Stone/maapind.png')
surface = pygame.transform.scale(surface,(96,96))

water_surface = pygame.Surface((1100,50))
water_surface.fill('Lightblue')
#player
player_surface = pygame.image.load('pildid/1 Pink_Monster/Pink_Monster.png')
player_surface = pygame.transform.scale(player_surface,(96,96))
player_rect = player_surface.get_rect(midbottom = (100,750))
player_gravitatsioon = 0





#Enemy image
bat_surface = pygame.image.load('pildid/Enemy sprites/bat_fly.png')



#Muutujad
scroll = 0
tiles1 = (ceil(SCREEN_WIDTH / bg1_width)) + 1
tiles2 = (ceil(SCREEN_WIDTH / bg2_width)) + 1
tiles3 = (ceil(SCREEN_WIDTH / bg3_width)) + 1


gravitatsioon = 0
#print(tiles1)
#print(tiles2)
#print(tiles3)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #Parem versioon run = True, sest Errori võimalus väiksem
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 750:
            player_gravitatsioon = -30
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 750:
                player_gravitatsioon = -30




    if game_active:
        for i in range(0,tiles1): #Paneb pildid üksteise kõrvale, järgisin tutoriali Coding With Russ "Infinite Scrolling Background"
            screen.blit(background1,(i * bg1_width + scroll,0))
            screen.blit(background2,(i * bg2_width + scroll,0))
            screen.blit(background3,(i * bg3_width + scroll,0))
        #Scroll background
        scroll -= 5
        #Resetib scrolli (muidu saab pilt otsa)
        if abs(scroll) > bg1_width:
            scroll = 0

        screen.blit(skoor_surface,skoor_rect)
        screen.blit(water_surface,(0,750))
        for i in range(0,SCREEN_WIDTH,100):
            screen.blit(surface,(i,750))
        
        player_gravitatsioon += 1
        player_rect.y += player_gravitatsioon

        if player_rect.bottom >= 750:
            player_rect.bottom = 750
    else:
        game_active = False


    screen.blit(player_surface,player_rect)
    screen.blit(bat_surface,(800,400))
    

    pygame.display.update()
    clock.tick(FPS)