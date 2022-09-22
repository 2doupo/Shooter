from random import randint
import pygame
from Enemy import Enemy
from Entity import Entity, EntityTag
class SimpleEnemy(Enemy):
    size=30
    speed=0.25
    shotspeed=0.7
    image=pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/SimpleEnemy.png'),(52,64))
    cooldown=400
    last_shot_time=-100
    dir=1
    pv=100
    color=(255,0,0)
    def __init__(self,entitys,scr,pos=(0,0)):
        super().__init__(entitys,scr,self.cooldown,pos,self.speed,self.image,self.shotspeed,EntityTag.SIMPLE_ENEMY)
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        
    def kill(self,entitys) -> None:
        super().kill(entitys)
    def update(self,entitys):
        
        
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        self.x+=self.dir*self.speed*entitys.dt
        self.pos=(self.x,self.y)
        
        super().update(entitys)
        
        #pygame.draw.circle(self.scr,self.color,self.pos,self.size/2)
        
        
