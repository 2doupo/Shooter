import pygame
from entity.Entity import Entity, EntityTag
import math
class Shot(Entity):
    team=None
        
    def __init__(self,entitys,shooter,pos,scr,size,speed,tag):
        self.tag=tag
        super().__init__(entitys,pos,scr,tag)
        self.screenw,self.screenh=640,800
        self.size=size
        self.speed=speed
        self.start_pos=pos
        self.start_time=pygame.time.get_ticks()
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        self.shooter=shooter
        

    def kill(self) -> None:
        super().kill()

    def update(self,entitys):
        
        
        if(self.tag==EntityTag.PLAYERSHOT):
            self.y+=-self.speed*entitys.dt
            col=(0,0,0)
        elif(self.tag==EntityTag.ENEMYSHOT) :
            col=(255,0,0)
            if(self.shooter.tag==EntityTag.MALICIOUS):

                self.x=self.start_pos[0]+75*math.sin((pygame.time.get_ticks()-self.start_time)/100)
                self.y+=self.speed*entitys.dt
            else:
                self.y+=self.speed*entitys.dt
        
        self.pos=(self.x,self.y)
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        if(((self.x<0)|(self.x>self.screenw))|((self.y<0)|(self.y>self.screenh))): self.kill()
        pygame.draw.circle(self.scr,col,self.pos,self.size)