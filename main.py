# Projekt Rupa, autor Karl Eerik Vaidla
# Mängu loomiseks on vaadatud erinevaid videoõpetusi
#
#




import pygame
from sys import exit
from math import ceil
from random import randint
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
FPS = 60
PLAYER_HEIGHT = 605
#Aja info
def timer():
    uusaeg = pygame.time.get_ticks() - starttime #Annab aja mängu algusest
    uusaeg = int(uusaeg/1000)
    aeg_surface = font2.render(f"Aeg: {uusaeg}",False,"Red")
    aeg_rect = aeg_surface.get_rect(center = (1000,100))
    screen.blit(aeg_surface,aeg_rect)

def player_animation(): #Funktsiooni loogika on loodud youtube:Clear Code poolt
    global player_surface, player_index

    if player_rect.bottom < PLAYER_HEIGHT:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


def obstaclemovement(obstacle_list): #Funktsiooni loogika on loodud youtube:Clear Code poolt
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            
            if obstacle_rect.bottom == 600:
                screen.blit(frog_jump_surface,obstacle_rect)
            

            elif obstacle_rect.bottom == 500:
                screen.blit(bat_fly_surface,obstacle_rect)  #selleks, et animeeritud oleks, on vaja asendada esimesele kohale surface
            elif obstacle_rect.bottom == 400:
                screen.blit(bee_fly_surface,obstacle_rect)
            if obstacle_rect.bottom == 601:
                screen.blit(barnacle1,obstacle_rect) 

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #Võtab listist ära, kui üle läheb üle -100, selleks, et mäng paremini töötaks


        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True



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

water_surface = pygame.Surface((1100,200))
water_surface.fill('Lightblue')

#player info
player_walk1 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Run_1.png')
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
player_walk = [player_Walk1,player_Walk1,player_Walk3,player_Walk4,player_Walk5,player_Walk6]


player_index = 0
player_jump = player_walk1 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Jump_1.png')
player_jump = pygame.transform.scale(player_jump,(96,96))
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (300,PLAYER_HEIGHT))
player_stand = pygame.image.load('pildid/1 Pink_Monster/Pink_Monster.png')
player_stand = pygame.transform.scale(player_stand,(96,96))
player_gravitatsioon = 0
#Vaenlaste pildid
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

frog_jump1 = pygame.image.load('pildid/Maincharacters/frog.png')
frog_jump2 = pygame.image.load('pildid/Maincharacters/frog_leap.png')
frog_jump = [frog_jump1,frog_jump2]
frog_jump_index = 0
frog_jump_surface = frog_jump[frog_jump_index]

barnacle1 = pygame.image.load('pildid/Maincharacters/barnacle_bite.png')

obstacle_rect_list = []

#Mündi pildid
coin1 = pygame.image.load('pildid/Maincharacters/coin1_16x16.png')
coin2 = pygame.image.load('pildid/Maincharacters/coin2_16x16.png')
coin3 = pygame.image.load('pildid/Maincharacters/coin3_16x16.png')
coin4 = pygame.image.load('pildid/Maincharacters/coin4_16x16.png')
coin5 = pygame.image.load('pildid/Maincharacters/coin5_16x16.png')
coin6 = pygame.image.load('pildid/Maincharacters/coin6_16x16.png')
coin7 = pygame.image.load('pildid/Maincharacters/coin7_16x16.png')
coin8 = pygame.image.load('pildid/Maincharacters/coin8_16x16.png')
coin9 = pygame.image.load('pildid/Maincharacters/coin9_16x16.png')
coin10 = pygame.image.load('pildid/Maincharacters/coin10_16x16.png')
coin = [coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,coin9,coin10]
#Muutujad
scroll = 0
tiles1 = (ceil(SCREEN_WIDTH / bg1_width)) + 1
tiles2 = (ceil(SCREEN_WIDTH / bg2_width)) + 1
tiles3 = (ceil(SCREEN_WIDTH / bg3_width)) + 1

starttime = 0
aeg = 0
gravitatsioon = 0
game_active = False

obstacle_timer = pygame.USEREVENT + 1 #+1 vaja selleks, kuna pygame endal ka vaja evente.
pygame.time.set_timer(obstacle_timer,1900)

bee_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bee_animation_timer,300)
bat_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bat_animation_timer,200)
frog_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(frog_animation_timer,600)


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
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= PLAYER_HEIGHT:
                player_gravitatsioon = -35

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= PLAYER_HEIGHT:
                    player_gravitatsioon = -35
                if event.key == pygame.K_s and player_rect.bottom < PLAYER_HEIGHT:
                    player_gravitatsioon = 50
            



            if event.type == obstacle_timer:
                randomnumber = randint(1,5)
                if randomnumber == 1:
                    obstacle_rect_list.append(bat_fly1.get_rect(bottomright = (randint(1100,1400),400)))
                elif randomnumber == 2:
                    obstacle_rect_list.append(bee_fly1.get_rect(bottomright = (randint(1100,1400),500)))
                elif randomnumber == 3:
                    obstacle_rect_list.append(frog_jump1.get_rect(bottomright = (randint(1100,1400),600)))
                elif randomnumber == 4:
                    obstacle_rect_list.append(barnacle1.get_rect(bottomright = (randint(1100,1400),601)))


            if event.type == bee_animation_timer:
                if bee_fly_index == 0:
                    bee_fly_index = 1
                else:
                    bee_fly_index = 0
                bee_fly_surface = bee_fly[bee_fly_index]
            if event.type == bat_animation_timer:
                if bat_fly_index == 0:
                    bat_fly_index = 1
                else:
                    bat_fly_index = 0
                bat_fly_surface = bat_fly[bat_fly_index]
                
            if event.type == frog_animation_timer:
                if frog_jump_index == 0:
                    frog_jump_index = 1
                else:
                    frog_jump_index = 0
            frog_jump_surface = frog_jump[frog_jump_index] 
                    
                    
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                starttime = int(pygame.time.get_ticks()/1000)



                


    if game_active:
        for i in range(0,tiles1): #Paneb pildid üksteise kõrvale, loogika on loodud youtube:Coding With Russ
            screen.blit(background1,(i * bg1_width + scroll,0))
            screen.blit(background2,(i * bg2_width + scroll,0))
            screen.blit(background3,(i * bg3_width + scroll,0))
        
        scroll -= 5
        #Resetib scrolli (muidu saab pilt otsa)
        if abs(scroll) > bg1_width:
            scroll = 0

        screen.blit(water_surface,(0,600))
        for i in range(0,SCREEN_WIDTH,100):
            for j in range(0,200,100):
                screen.blit(surface,(i,600 + j))
        
        player_gravitatsioon += 1
        player_rect.y += player_gravitatsioon

        if player_rect.bottom >= PLAYER_HEIGHT:
            player_rect.bottom = PLAYER_HEIGHT

        player_animation()
        screen.blit(player_surface,player_rect)


        obstacle_rect_list = obstaclemovement(obstacle_rect_list)
        game_active = collisions(player_rect,obstacle_rect_list)
        timer()
        
    else:
        screen.fill(("Lightblue"))
        screen.blit(player_stand,(200,300))
        obstacle_rect_list.clear() #Selleks, et peale collisioni saaks uuesti mängu tööle panna
        player_rect.midbottom = (80,300)
        player_gravitatsioon = 0

    
    
    

    pygame.display.update()
    clock.tick(FPS)