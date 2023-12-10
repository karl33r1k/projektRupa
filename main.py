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

#Tausta pildi info
background1 = pygame.image.load('pildid/taust/background1.png')
background1 = pygame.transform.scale(background1,(1000,800))
background2 = pygame.image.load('pildid/taust/background2.png')
background2 = pygame.transform.scale(background2,(1000,800))
background3 = pygame.image.load('pildid/taust/background3.png')
background3 = pygame.transform.scale(background3,(1000,800))

bg1_width = background1.get_width()
bg2_width = background2.get_width()
bg3_width = background3.get_width()

#Font info
font1 = pygame.font.Font('Retro Gaming.ttf',50)
font2 = pygame.font.Font('Retro Gaming.ttf',30)

#Maapinna info
surface = pygame.image.load('pildid/Stone/maapind.png')
surface = pygame.transform.scale(surface,(96,96))

water_surface = pygame.Surface((1100,50))
water_surface.fill('Lightblue')

#player info
player_surface = pygame.image.load('pildid/1 Pink_Monster/Pink_Monster.png')
player_surface = pygame.transform.scale(player_surface,(96,96))
player_rect = player_surface.get_rect(midbottom = (100,750))



player_gravitatsioon = 0
game_active = False

#Vaenlaste pildid
bat_surface = pygame.image.load('pildid/Enemy sprites/bat_fly.png')

#Muutujad
scroll = 0
tiles1 = (ceil(SCREEN_WIDTH / bg1_width)) + 1
tiles2 = (ceil(SCREEN_WIDTH / bg2_width)) + 1
tiles3 = (ceil(SCREEN_WIDTH / bg3_width)) + 1

starttime = 0
aeg = 0
gravitatsioon = 0
game_active = False

#Aja info
def aeg():
    aeg = pygame.time.get_ticks() - starttime #Annab aja mängu algusest
    aeg = int(aeg/1000)
    aeg_surface = font2.render(f"Aeg: {aeg}",False,"Red")
    aeg_rect = aeg_surface.get_rect(center = (1000,100))
    screen.blit(aeg_surface,aeg_rect)
    return aeg
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #Parem versioonist run = True, sest Errori võimalus väiksem
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 750:
                player_gravitatsioon = -30 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 750:
                    player_gravitatsioon = -30
                if event.key == pygame.K_s and player_rect.bottom < 750:
                    player_gravitatsioon = 0.1
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                starttime = int(pygame.time.get_ticks()/1000)

    if game_active:
        for i in range(0,tiles1): #Paneb pildid üksteise kõrvale, järgisin tutoriali Coding With Russ "Infinite Scrolling Background"
            screen.blit(background1,(i * bg1_width + scroll,0))
            screen.blit(background2,(i * bg2_width + scroll,0))
            screen.blit(background3,(i * bg3_width + scroll,0))
        
        scroll -= 5
        #Resetib scrolli (muidu saab pilt otsa)
        if abs(scroll) > bg1_width:
            scroll = 0

        screen.blit(water_surface,(0,750))
        for i in range(0,SCREEN_WIDTH,100):
            screen.blit(surface,(i,750))
        
        player_gravitatsioon += 1
        player_rect.y += player_gravitatsioon

        if player_rect.bottom >= 750:
            player_rect.bottom = 750

        screen.blit(player_surface,player_rect)


        screen.blit(bat_surface,(800,400))


        aeg()



        
    else:
        screen.fill((94,129,162))
        screen.blit(player_surface,(200,300))

    
    
    

    pygame.display.update()
    clock.tick(FPS)