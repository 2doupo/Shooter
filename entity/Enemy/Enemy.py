
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
    cd_move=50
    touch=False
    
    
    
    def __init__(self,entitys,scr,cool=300,pos=(0,0),side_speed=0,down_speed=0,image: pygame.surface.Surface=None,shotspeed=1,tag=None):
        super().__init__(entitys,pos,scr,tag)
        self.side_speed=side_speed
        self.down_speed=down_speed
        self.shotspeed=shotspeed
        self.cooldown=cool
        self.image=image
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
        self.last_move_time=0
        
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
    
    def endmove_cd(self):
        return pygame.time.get_ticks()-self.last_move_time>self.cd_move
      
        
    def kill(self,entitys) -> None:
        entitys.killcount+=1
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
        if(self.tag not in [EntityTag.BOSS,EntityTag.MALICIOUS]):

            self.y+=self.down_speed*entitys.dt
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
        shot=pygame.sprite.spritecollide(self,entitys.player_shots,True)
        if(shot.__len__()!=0):
            self.touch=True
        else:
            self.touch=False
        if(len(shot)!=0):
            self.pv+=-10
        if(self.pv<=0):
            self.kill(entitys)
        if(self.touch):
            self.scr.blit(self.image,self.rect,special_flags=pygame.BLEND_ADD)
        else:
            self.scr.blit(self.image,self.rect)

        
        
        



