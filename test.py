# Projekt Rupa, autor Karl Eerik Vaidla
# Mängu loomiseks on vaadatud erinevaid videoõpetusi
#
#




import pygame
from sys import exit
from math import ceil
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.player_walk = [player_Walk1,player_Walk2,player_Walk3,player_Walk4,player_Walk5,player_Walk6]

        self.player_index = 0
        player_jump = player_walk1 = pygame.image.load('pildid/Maincharacters/Pink_Monster_Jump_1.png')
        self.player_jump = pygame.transform.scale(player_jump,(96,96))



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

def obstaclecollision():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Jooksja")
clock = pygame.time.Clock()

#Sprite grupid
player = pygame.sprite.GroupSingle() #Kuna Player on ainuke yksus, siis GroupSingle
player.add(Player())

obstacle_group = pygame.sprite.Group() #Kuna mitu yksust, siis vaja Group ning ei kasuta "add" kohe, sest tahame, et timer "triggeriks" obstaclesid







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



#Playeri valik
player_stand = pygame.image.load('pildid/1 Pink_Monster/Pink_Monster.png')
player_stand = pygame.transform.scale(player_stand,(96,96))
player_gravitatsioon = 0

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
ladybug_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(ladybug_animation_timer,1500)


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
                
            if event.type == ladybug_animation_timer:
                if ladybug_walk_index == 0:
                    ladybug_walk_index = 1
                else:
                    ladybug_walk_index = 0
            ladybug_walk_surface = ladybug_walk[ladybug_walk_index] 
                    
                    
            
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
        
        # player_gravitatsioon += 1
        # player_rect.y += player_gravitatsioon

        # if player_rect.bottom >= PLAYER_HEIGHT:
        #     player_rect.bottom = PLAYER_HEIGHT

        # player_animation()
        # screen.blit(player_surface,player_rect)

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()



        # obstacle_rect_list = obstaclemovement(obstacle_rect_list)
        game_active = obstaclecollision()
        timer()
        
    else:
        screen.fill(("Lightblue"))
        screen.blit(player_stand,(200,300))
        player_gravitatsioon = 0

    
    
    

    pygame.display.update()
    clock.tick(FPS)