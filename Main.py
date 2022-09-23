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

level1=Level(screen,screenwidth,screenheight)


pygame.init()
pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(32,32)))
arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)

run = True
while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        level1.update()
        
        fps=arial.render("fps :" + str(int(level1.clock.get_fps())),False,(0,0,0),(255,255,255))
        screen.blit(fps,(screenwidth-70,screenheight-30))
        
        #print(clock.get_time())
        
        #ms_par_frame=arial.render(str(clock.get_time()),False,(0,0,0))
        #screen.blit(ms_par_frame,(screenwidth-60,screenheight-60))
        #print(entint.enemy_shots.__len__(),entint.player_shots.__len__())
        #print(shield.pos)
        #print(entint.items)
        pygame.display.update()
        
        
        


        

pygame.quit() 
quit()