
from random import randint
import pygame
from entity.item.DoubleShot import DShot
from entity.item.Shield import Shield
from entity.Shot import Shot
from entity.Entity import Entity,EntityTag
from entity.item.CadenceUp import CadUp
from entity.item.Heal import Heal

class Enemy(Entity):
   
    last_shot_time=-100
    pv=100
    
    def __init__(self,entitys,scr,cool=300,pos=(0,0),speed=0,image: pygame.surface.Surface=None,shotspeed=1,tag=None):
        super().__init__(entitys,pos,scr,tag)
        self.speed=speed
        self.shotspeed=shotspeed
        self.cooldown=cool
        self.image=image
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
        
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
      
        
    def kill(self,entitys) -> None:
        super().kill()
        if(randint(1,100)<=50):
            temp=randint(1,100)
            if(temp<=25):
                CadUp(entitys,self.pos,self.scr)
            elif(25<temp<=50):
                Heal(entitys,self.pos,self.scr)
            elif(50<temp<=75):
                DShot(entitys,self.pos,self.scr)
            else: 
                Shield(entitys,self.pos,self.scr)

    def update(self,entitys):
        
        super().update(entitys)
        if(self.endcooldown()):
            Shot(entitys,(self.x,self.y+self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.ENEMYSHOT)
            self.last_shot_time=pygame.time.get_ticks()
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
        shot=pygame.sprite.spritecollide(self,entitys.player_shots,True)
        if(len(shot)!=0):
            self.pv+=-10
        if(self.pv<=0):
            self.kill(entitys)
        self.scr.blit(self.image,self.rect)
        
        
        



