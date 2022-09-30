from os.path import exists
import pickle
import pygame
pygame.init()
screenwidth=640
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight),vsync=1)

from Savedata import Savedata
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

savedata=Savedata()

if(exists('Save/save.douteau')):
        savedata=pickle.load(open('Save/save.douteau','rb'))
else:
        pickle.dump(savedata,open('Save/save.douteau','wb'))
run = True
in_menu = True
in_level= False
level=Level(screen,screenwidth,screenheight,savedata)
menu=Menu(screen,screenwidth,screenheight)
water=pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/Watergreen.jpg')
w1=water.get_width()
w2=water.get_height()
scale=3.5
water=pygame.transform.scale(water,(w1*scale,w2*scale))
pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(32,32)))
arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
y=0
backspeed=0.5


while run:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        
        y+=backspeed
        for i in range(int(screenwidth/water.get_width())+1):
                for j in range(-1,int(screenheight/water.get_height())+1):
                        screen.blit(water,(i*water.get_width(),(j*water.get_height()+y)%(screenheight+water.get_height())-water.get_height()))
        if(in_menu):
                menu.update()
                
                if(menu.start_level):
                        in_level=True
                        in_menu=False
                        level.start()
        elif(in_level):
                level.update()

                
        pygame.display.update()
        
savedata.save()
pygame.quit() 
quit()