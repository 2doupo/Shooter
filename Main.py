import pygame
pygame.init()
screenwidth=640
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight),vsync=1)


from random import randint
from entity.item.CadenceUp import CadUp
from entity.item.DoubleShot import DShot
from entity.item.Shield import Shield
from entity.Player import Player
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.Enemy.Malicious import Malicious
from entity.Enemy.Boss import Boss
from entity.Entity import EntInt,EntityTag
from Level import Level
from Menu import Menu
run = True
in_menu = True
in_level= False
level=Level(screen,screenwidth,screenheight)
menu=Menu(screen,screenwidth,screenheight,run)
Player(level.entint,scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2))
Player(level.entint,scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g))

pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(32,32)))
arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)


while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if(in_menu):
                menu.update()
                run=menu.run
                if(menu.start_level):
                        in_level=True
                        in_menu=False
                        level.start()
        elif(in_level):
                level.update()

                
        
        
       
        pygame.display.update()
        

pygame.quit() 
quit()