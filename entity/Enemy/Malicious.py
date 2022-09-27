from random import randint
import pygame
from entity.Enemy.Enemy import Enemy
from entity.Entity import Entity, EntityTag
from entity.Shot import Shot
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
    def __init__(self,entitys,scr,pos=(0,0)):
        super().__init__(entitys,scr,self.cooldown,pos,self.speed,self.image,self.shotspeed,EntityTag.MALICIOUS)
    
    def kill(self,entitys) -> None:
        super().kill(entitys)
    def update(self,entitys):
        
        
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        
        elif(pygame.time.get_ticks()-self.last_dir_change>self.cooldown_dir_change):
            self.last_dir_change=pygame.time.get_ticks()
            if(randint(1,100)<=30): 
                self.dir*=-1

        self.x+=self.dir*self.speed*entitys.dt
        self.pos=(self.x,self.y)
        if(self.endcooldown()):
            Shot(entitys,(self.x,self.y+self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.ENEMYSHOT)
            self.last_shot_time=pygame.time.get_ticks()
        super().update(entitys)
        