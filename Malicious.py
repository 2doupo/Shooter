from random import randint
import pygame
from Enemy import Enemy
from Entity import Entity, EntityTag
class Malicious(Enemy):
    size=52
    image=pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(size,size))
    speed=0.25
    shotspeed=0.7
    cooldown=1000
    last_shot_time=-100
    cooldown_dir_change=300
    last_dir_change=-100
    dir=1
    pv=100
    def __init__(self,scr,pos=(0,0)):
        super().__init__(scr,self.cooldown,pos,self.speed,self.image,self.shotspeed,EntityTag.MALICIOUS)
    

    def update(self,enemy_shots,player_shots,items,dt):
        
        
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        
        elif(pygame.time.get_ticks()-self.last_dir_change>self.cooldown_dir_change):
            self.last_dir_change=pygame.time.get_ticks()
            if(randint(1,100)<=30): 
                self.dir*=-1

        self.x+=self.dir*self.speed*dt
        self.pos=(self.x,self.y)

        super().update(enemy_shots,player_shots,items,dt)
        