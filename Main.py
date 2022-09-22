import pygame
pygame.init()
screenwidth=640
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight))
from random import randint
from CadenceUp import CadUp
from DoubleShot import DShot
from Player import Player
from SimpleEnemy import SimpleEnemy
from Malicious import Malicious
from Boss import Boss
from Entity import EntInt,EntityTag

pygame.init()
screenwidth=640
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight),vsync=1)
entint=EntInt()

pygame.init()
pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(32,32)))
arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
bossfight=False 

Player(entint,scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2))
Player(entint,scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g))

#players.add(Player(scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_k,pygame.K_i,pygame.K_j,pygame.K_l,pygame.K_m)))

maliciousnb=5
for i in range(maliciousnb):
        Malicious(entint,screen,(screenwidth/2,50))
SimpleEnemy(entint,screen,(screenwidth/2,50))

DShot(entint,(50,400),screen)
CadUp(entint,(50,200),screen)

clock=pygame.time.Clock()
run = True
while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        dt = clock.tick(120)
        pygame.draw.rect(screen, (135,206,235), pygame.Rect(0,0,screenwidth, screenheight))
        
        entint.update(dt)

        if(len(entint.players)==0):
                #run=False
                game_over=bigarial.render("Game Over",False,(0,0,0))
                
                screen.blit(game_over,((screenwidth-game_over.get_width())/2,screenheight/2))

        if((entint.enemys.__len__()==0)& (not bossfight)):
                entint.add(Boss(entint,screen,(screenwidth/2,100)))
                bossfight=True
        elif((entint.enemys.__len__()==0)& (bossfight)):
                run=False
        
        fps=arial.render("fps :" + str(int(clock.get_fps())),False,(0,0,0),(255,255,255))
        screen.blit(fps,(screenwidth-70,screenheight-30))
        
        #print(clock.get_time())
        
        #ms_par_frame=arial.render(str(clock.get_time()),False,(0,0,0))
        #screen.blit(ms_par_frame,(screenwidth-60,screenheight-60))
        #print(entint.enemy_shots.__len__(),entint.player_shots.__len__())
        pygame.display.update()
        
        
        


        

pygame.quit() 
quit()