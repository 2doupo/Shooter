from random import randint
import pygame
from entity.Enemy.Enemy import Enemy
from entity.Entity import Entity, EntityTag
from entity.Shot import Shot
class SimpleEnemy(Enemy):
    size=30
    side_speed=0.25
    down_speed=0.02
    shotspeed=0.7
    image=pygame.transform.scale(pygame.image.load('Image/SimpleEnemy.png'),(52,64))
    cooldown=400
    last_shot_time=-100
    dir=1
    pv=100
    color=(255,0,0)
    def __init__(self,entitys,scr,pos=(0,0)):
        super().__init__(entitys,scr,self.cooldown,pos,self.side_speed,self.down_speed,self.image,self.shotspeed,EntityTag.SIMPLE_ENEMY)
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        
    def kill(self,entitys) -> None:
        super().kill(entitys)
    def update(self,entitys):
        
        
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        self.x+=self.dir*self.side_speed*entitys.dt
        self.pos=(self.x,self.y)
        
        if(self.endcooldown()):
            Shot(entitys,(self.x,self.y+self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.ENEMYSHOT)
            self.last_shot_time=pygame.time.get_ticks()
        super().update(entitys)
        
        #pygame.draw.circle(self.scr,self.color,self.pos,self.size/2)
        
        
