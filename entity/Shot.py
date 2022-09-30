import pygame
from entity.Entity import Entity, EntityTag
class Shot(Entity):
    team=None
    screenw,screenh=pygame.display.get_window_size()
    def __init__(self,entitys,pos,scr,size,speed,tag):
        self.tag=tag
        super().__init__(entitys,pos,scr,tag)
        self.size=size
        self.speed=speed
        
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        

    def kill(self) -> None:
        super().kill()
    def update(self,entitys):
        
        
        if(self.tag==EntityTag.PLAYERSHOT):
            self.y+=-self.speed*entitys.dt
            col=(0,0,0)
        elif(self.tag==EntityTag.ENEMYSHOT) :
            self.y+=self.speed*entitys.dt
            col=(255,0,0)
        self.pos=(self.x,self.y)
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        if(((self.x<0)|(self.x>self.screenw))|((self.y<0)|(self.y>self.screenh))): self.kill()
        pygame.draw.circle(self.scr,col,self.pos,self.size)