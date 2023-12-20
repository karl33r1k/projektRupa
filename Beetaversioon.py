# Projekt Rupa, autor Karl Eerik Vaidla
# Mängu loomiseks on vaadatud erinevaid videoõpetusi (YT: Clear Code ja Coding with Russ)
# Allikad README failis

import pygame
from sys import exit
from math import ceil
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self,playertype):
        super().__init__()
        
        if playertype == 1:
            player_walk1 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_1.png') #Oleks saanud kasutada ka spritesheeti
            player_Walk1 = pygame.transform.scale(player_walk1,(96,96))
            player_walk2 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_2.png')
            player_Walk2 = pygame.transform.scale(player_walk2,(96,96))
            player_walk3 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_3.png')
            player_Walk3 = pygame.transform.scale(player_walk3,(96,96))
            player_walk4 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_4.png')
            player_Walk4 = pygame.transform.scale(player_walk4,(96,96))
            player_walk5 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_5.png')
            player_Walk5 = pygame.transform.scale(player_walk5,(96,96))
            player_walk6 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_6.png')
            player_Walk6 = pygame.transform.scale(player_walk6,(96,96))
            player_jump = player_walk1 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Jump_1.png')
            self.player_jump = pygame.transform.scale(player_jump,(96,96))
            self.player_walk = [player_Walk1,player_Walk2,player_Walk3,player_Walk4,player_Walk5,player_Walk6]
        elif playertype == 2:
            player_walk1 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_1.png')
            player_Walk1 = pygame.transform.scale(player_walk1,(96,96))
            player_walk2 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_2.png')
            player_Walk2 = pygame.transform.scale(player_walk2,(96,96))
            player_walk3 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_3.png')
            player_Walk3 = pygame.transform.scale(player_walk3,(96,96))
            player_walk4 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_4.png')
            player_Walk4 = pygame.transform.scale(player_walk4,(96,96))
            player_walk5 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_5.png')
            player_Walk5 = pygame.transform.scale(player_walk5,(96,96))
            player_walk6 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Run_6.png')
            player_Walk6 = pygame.transform.scale(player_walk6,(96,96))
            player_jump = player_walk1 = pygame.image.load('pildid/Maincharacters/Owlet_Monster_Jump_1.png')
            self.player_jump = pygame.transform.scale(player_jump,(96,96))
            self.player_walk = [player_Walk1,player_Walk2,player_Walk3,player_Walk4,player_Walk5,player_Walk6]
        elif playertype == 3:
            player_walk1 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_1.png')
            player_Walk1 = pygame.transform.scale(player_walk1,(96,96))
            player_walk2 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_2.png')
            player_Walk2 = pygame.transform.scale(player_walk2,(96,96))
            player_walk3 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_3.png')
            player_Walk3 = pygame.transform.scale(player_walk3,(96,96))
            player_walk4 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_4.png')
            player_Walk4 = pygame.transform.scale(player_walk4,(96,96))
            player_walk5 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_5.png')
            player_Walk5 = pygame.transform.scale(player_walk5,(96,96))
            player_walk6 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Run_6.png')
            player_Walk6 = pygame.transform.scale(player_walk6,(96,96))
            player_jump = player_walk1 = pygame.image.load('pildid/Maincharacters/Dude_Monster_Jump_1.png')
            self.player_jump = pygame.transform.scale(player_jump,(96,96))
            self.player_walk = [player_Walk1,player_Walk2,player_Walk3,player_Walk4,player_Walk5,player_Walk6]
    
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200,600))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= PLAYER_HEIGHT:
            self.gravity = -35
        if keys[pygame.MOUSEBUTTONDOWN] and self.rect.bottom >= PLAYER_HEIGHT:
            self.gravity = -35
        if keys[pygame.K_s] and self.rect.bottom < PLAYER_HEIGHT:
            self.gravity = 50

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= PLAYER_HEIGHT:
            self.rect.bottom = PLAYER_HEIGHT

    def animation(self):
        if self.rect.bottom < PLAYER_HEIGHT:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()



class Obstacle(pygame.sprite.Sprite):
    def __init__(self,obstacletype):
        super().__init__()

        if obstacletype == 'bee':
            bee_fly1 = pygame.image.load('pildid/Maincharacters/bee_fly.png')
            bee_fly2 = pygame.image.load('pildid/Maincharacters/bee.png')
            self.frames = [bee_fly1,bee_fly2]
            y_position = 500
        elif obstacletype == "bat":
            bat_fly1 = pygame.image.load('pildid/Maincharacters/bat_fly.png')
            bat_fly2 = pygame.image.load('pildid/Maincharacters/bat_hang.png')
            self.frames = [bat_fly1,bat_fly2]
            y_position = 400
        elif obstacletype == "barnacle":
            barnacle = pygame.image.load('pildid/Maincharacters/barnacle_bite.png')
            self.frames = [barnacle]
            y_position = 601
        elif obstacletype == "ladybug":
            ladybug_walk1 = pygame.image.load('pildid/Maincharacters/ladyBug.png')
            ladybug_walk2 = pygame.image.load('pildid/Maincharacters/ladyBug_walk.png')
            self.frames = [ladybug_walk1,ladybug_walk2]
            y_position = 600
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(1100,1400),y_position))

    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation()
        self.rect.x -= 5
        self.destroy()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin1 = pygame.image.load('pildid/Maincharacters/coin1_16x16.png')
        coin1 = pygame.transform.scale(coin1,(64,64))
        coin2 = pygame.image.load('pildid/Maincharacters/coin2_16x16.png')
        coin2 = pygame.transform.scale(coin2,(64,64))
        coin3 = pygame.image.load('pildid/Maincharacters/coin3_16x16.png')
        coin3 = pygame.transform.scale(coin3,(64,64))
        coin4 = pygame.image.load('pildid/Maincharacters/coin4_16x16.png')
        coin4 = pygame.transform.scale(coin4,(64,64))
        coin5 = pygame.image.load('pildid/Maincharacters/coin5_16x16.png')
        coin5 = pygame.transform.scale(coin5,(64,64))
        coin6 = pygame.image.load('pildid/Maincharacters/coin6_16x16.png')
        coin6 = pygame.transform.scale(coin6,(64,64))
        coin7 = pygame.image.load('pildid/Maincharacters/coin7_16x16.png')
        coin7 = pygame.transform.scale(coin7,(64,64))
        coin8 = pygame.image.load('pildid/Maincharacters/coin8_16x16.png')
        coin8 = pygame.transform.scale(coin8,(64,64))
        coin9 = pygame.image.load('pildid/Maincharacters/coin9_16x16.png')
        coin9 = pygame.transform.scale(coin9,(64,64))
        coin10 = pygame.image.load('pildid/Maincharacters/coin10_16x16.png')
        coin10 = pygame.transform.scale(coin10,(64,64))
        self.coins = [coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,coin9,coin10]
        self.coin_index = 0
        y_position = 600

        self.image = self.coins[self.coin_index]
        self.rect = self.image.get_rect(midbottom = (randint(1200,1300),y_position))

    def animation(self):
        self.coin_index += 0.1
        if self.coin_index >= len(self.coins):
            self.coin_index = 0
        self.image = self.coins[int(self.coin_index)]
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation()
        self.rect.x -= 5
        self.destroy()

#Muutujad1
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
FPS = 60
PLAYER_HEIGHT = 605

#Aja info
def timer():
    uusaeg = pygame.time.get_ticks() - starttime #Annab aja mängu algusest
    uusaeg = int(uusaeg/1000)
    aeg_surface = font2.render(f"Time: {uusaeg}",False,"Red")
    aeg_rect = aeg_surface.get_rect(center = (80,100))
    screen.blit(aeg_surface,aeg_rect)
#Punktide teksti kuvamine
def coinvalue():
    coinpoint_surface = font2.render(f"Points: {coinpoint}",False,"Blue")
    coinpoint_rect = coinpoint_surface.get_rect(center = (110,150)) 
    screen.blit(coinpoint_surface,coinpoint_rect)

#Koletiste collision funktsioon
def obstaclecollision():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False,pygame.sprite.collide_mask):
        obstacle_group.empty()
        return False
    else:
        return True
#Mündi collision funktsioon
def coincollision():
    global coinpoint
    if pygame.sprite.spritecollide(player.sprite,coinsgrp,True,pygame.sprite.collide_mask): #Kolmas faktor määrab selle, et coin kaob kokkupuutel ära, neljas faktor teeb collisioni täpsemaks
        coinpoint += 100
        return False
    else:
        return True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Rupa Runner")
clock = pygame.time.Clock()

#Sprite grupid
player = pygame.sprite.GroupSingle() #Kuna Player on ainuke yksus, siis GroupSingle

obstacle_group = pygame.sprite.Group() #Kuna mitu yksust, siis vaja Group ning ei kasuta "add" kohe, sest tahame, et timer "triggeriks" obstaclesid

coinsgrp = pygame.sprite.GroupSingle()
coinsgrp.add(Coin())

#Font info
font1 = pygame.font.Font('Retro Gaming.ttf',50)
font2 = pygame.font.Font('Retro Gaming.ttf',30)
font3 = pygame.font.Font('Retro Gaming.ttf',45)

#Maapinna info
surface = pygame.image.load('pildid/Stone/maapind.png')
surface = pygame.transform.scale(surface,(96,96))

water_surface = pygame.Surface((1100,200))
water_surface.fill('Lightblue')
#Taust

background11 = pygame.image.load('pildid/taust/taust1/background1.png')
background11 = pygame.transform.scale(background11,(1000,800))
background21 = pygame.image.load('pildid/taust/taust1/background2.png')
background21 = pygame.transform.scale(background21,(1000,800))
background31 = pygame.image.load('pildid/taust/taust1/background3.png')
background31 = pygame.transform.scale(background31,(1000,800))
bg11_width = background11.get_width()
tiles11 = (ceil(SCREEN_WIDTH / bg11_width)) + 1
background12 = pygame.image.load('pildid/taust/taust2/background1.png')
background12 = pygame.transform.scale(background12,(1000,800))
background22 = pygame.image.load('pildid/taust/taust2/background2.png')
background22 = pygame.transform.scale(background22,(1000,800))
background32 = pygame.image.load('pildid/taust/taust2/background3.png')
background32 = pygame.transform.scale(background32,(1000,800))
bg12_width = background12.get_width()
tiles12 = (ceil(SCREEN_WIDTH / bg12_width)) + 1
#Playeri valik
player_stand1 = pygame.image.load('pildid/1 Pink_Monster/Pink_Monster.png')
player_stand1 = pygame.transform.scale(player_stand1,(96,96))
playerstand_rect1 = player_stand1.get_rect(midtop = (416,200))

player_stand2 = pygame.image.load('pildid/2 Owlet_Monster/Owlet_Monster.png')
player_stand2 = pygame.transform.scale(player_stand2,(96,96))
playerstand_rect2 = player_stand2.get_rect(midtop = (566,200))

player_stand3 = pygame.image.load('pildid/3 Dude_Monster/Dude_Monster.png')
player_stand3 = pygame.transform.scale(player_stand3,(96,96))
playerstand_rect3 = player_stand3.get_rect(midtop = (716,200))

#Menüü kastid
def text(fontsuurus,text,x,y,color):
    font = pygame.font.Font('Retro Gaming.ttf',fontsuurus)
    text_surface = font.render(text,False,color)
    text_rect = text_surface.get_rect(center = (x,y))
    screen.blit(text_surface,text_rect)


def kast(x,y,x1,y1,color):
    kast_surface = pygame.Surface((x,y))
    kast_surface.fill(color)
    screen.blit(kast_surface,(x1,y1))

exittext_surface = font3.render("Exit",False,"Black") #Selleks, et Exiti nupust rect argument tuleks, kirjutan selle eraldi välja
exittext_rect = exittext_surface.get_rect(center = (550,700))

#Worldmenu
planet1_surface = pygame.image.load('pildid/Maincharacters/planet05.png')
planet1_surface = pygame.transform.scale(planet1_surface,(320,320))
planet1_rect = planet1_surface.get_rect(midtop = (300,400))

planet2_surface = pygame.image.load('pildid/Maincharacters/planet07.png')
planet2_surface = pygame.transform.scale(planet2_surface,(320,320))
planet2_rect = planet2_surface.get_rect(midtop = (800,400))


#vaenlased
bat_fly1 = pygame.image.load('pildid/Maincharacters/bat_fly.png')
bat_fly2 = pygame.image.load('pildid/Maincharacters/bat_hang.png')
bat_fly = [bat_fly1,bat_fly2]
bat_fly_index = 0
bat_fly_surface = bat_fly[bat_fly_index]

bee_fly1 = pygame.image.load('pildid/Maincharacters/bee_fly.png')
bee_fly2 = pygame.image.load('pildid/Maincharacters/bee.png')
bee_fly = [bee_fly1,bee_fly2]
bee_fly_index = 0
bee_fly_surface = bee_fly[bee_fly_index]

ladybug_walk1 = pygame.image.load('pildid/Maincharacters/ladyBug.png')
ladybug_walk2 = pygame.image.load('pildid/Maincharacters/ladyBug_walk.png')
ladybug_walk = [ladybug_walk1,ladybug_walk2]
ladybug_walk_index = 0
ladybug_walk_surface = ladybug_walk[ladybug_walk_index]

barnacle1 = pygame.image.load('pildid/Maincharacters/barnacle_bite.png')

#Muutujad2



scroll = 0
coinpoint = 0
starttime = 0
game_active = False
worldmenu_active = False

obstacle_timer = pygame.USEREVENT + 1 #+1 vaja selleks, kuna pygame endal ka vaja evente.
pygame.time.set_timer(obstacle_timer,1900)
bee_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bee_animation_timer,300)
bat_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bat_animation_timer,200)
ladybug_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(ladybug_animation_timer,1500)
coin_animation_timer = pygame.USEREVENT + 5
pygame.time.set_timer(coin_animation_timer,12000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #Parem versioonist "run = True"-st, sest Errori võimalus väiksem
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['bee','bat','ladybug','barnacle'])))
            if event.type == coin_animation_timer:
                coinsgrp.add(Coin())
            
        else:
            pos = pygame.mouse.get_pos()
            if worldmenu_active:
                if planet1_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        worldtype = 1
                        worldmenu_active = False
                        game_active = True
                        starttime = int(pygame.time.get_ticks()/1000)
                if planet2_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        worldtype = 2
                        worldmenu_active = False
                        game_active = True
                        starttime = int(pygame.time.get_ticks()/1000)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        worldtype = 1
                        worldmenu_active = False
                        game_active = True
                        starttime = int(pygame.time.get_ticks()/1000)
                    elif event.key == pygame.K_2:
                        worldtype = 2
                        worldmenu_active = False
                        game_active = True
                        starttime = int(pygame.time.get_ticks()/1000)
                if exittext_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        pygame.quit()
                        exit()

            else:
                if playerstand_rect1.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        player.add(Player(1))
                        worldmenu_active = True
                if playerstand_rect2.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        player.add(Player(2))
                        worldmenu_active = True
                if playerstand_rect3.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        player.add(Player(3))
                        worldmenu_active = True
                if exittext_rect.collidepoint(pos):
                    if pygame.mouse.get_pressed() == (True,False,False):
                        pygame.quit()
                        exit()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        player.add(Player(1))
                        worldmenu_active = True
                    elif event.key == pygame.K_2:
                        player.add(Player(2))
                        worldmenu_active = True
                    elif event.key == pygame.K_3:
                        player.add(Player(3))
                        worldmenu_active = True
    if game_active:
        for i in range(0,tiles11): #Paneb pildid üksteise kõrvale, loogika on loodud youtube:Coding With Russ
            if worldtype == 1:
                screen.blit(background11,(i * bg11_width + scroll,0))
                screen.blit(background21,(i * bg11_width + scroll,0))
                screen.blit(background31,(i * bg11_width + scroll,0))
            elif worldtype == 2:
                screen.blit(background12,(i * bg12_width + scroll,0))
                screen.blit(background22,(i * bg12_width + scroll,0))
                screen.blit(background32,(i * bg12_width + scroll,0))
        scroll -= 5
        
        #Resetib scrolli (muidu saab pilt otsa)
        if abs(scroll) > bg11_width:
            scroll = 0

        screen.blit(water_surface,(0,600))
        for i in range(0,SCREEN_WIDTH,100):
            for j in range(0,200,100):
                screen.blit(surface,(i,600 + j))

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        coinsgrp.draw(screen)
        coinsgrp.update()

        coincollision()
        game_active = obstaclecollision()
        timer()
        coinvalue()
    elif worldmenu_active:
        screen.fill(("lightgreen"))
        kast(700,100,200,50,"Black")
        kast(680,80,210,60,"#93E9BE")
        text(80,"Choose world",550,99,"Black")
        text(45,"1",300,380,"Black")
        text(45,"2",800,380,"Black")
        #esimese planeedi kast
        kast(320,320,140,400,"Black")
        kast(300,300,150,410,"#93E9BE")
        #teise planeedi kast
        kast(320,320,640,400,"Black")
        kast(300,300,650,410,"#93E9BE")
        screen.blit(planet1_surface,planet1_rect)
        screen.blit(planet2_surface,planet2_rect)
        kast(150,60,475,670,"Black")
        kast(140,50,480,675,"#93E9BE")
        screen.blit(exittext_surface,exittext_rect)

    else:
        screen.fill(("lightgreen"))
        kast(96,96,368,208,"Black")
        kast(80,80,376,216,"#93E9BE")
        
        kast(96,96,518,208,"Black")
        kast(80,80,526,216,"#93E9BE")

        kast(96,96,668,208,"Black")
        kast(80,80,676,216,"#93E9BE")
        screen.blit(player_stand1,playerstand_rect1)
        screen.blit(player_stand2,playerstand_rect2)
        screen.blit(player_stand3,playerstand_rect3)

        kast(700,100,200,50,"Black")
        kast(680,80,210,60,"#93E9BE")

        text(80,"Rupa Runner",550,99,"Black") #y = 99, et p ära mahuks
        text(45,"1",416,190,"Black")
        text(45,"2",566,190,"Black")
        text(45,"3",716,190,"Black")
        kast(150,60,475,670,"Black")
        kast(140,50,480,675,"#93E9BE")
        screen.blit(exittext_surface,exittext_rect)
        coinpoint = 0
        

    pygame.display.update()
    clock.tick(FPS)