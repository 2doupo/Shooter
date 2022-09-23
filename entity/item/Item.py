from entity.Entity import Entity
import pygame

class Item(Entity):
    fallspeed=0.25
    
    def __init__(self,entitys,pos=(0,0),scr : pygame.surface.Surface=None,size=40,tag=None):
        super().__init__(entitys,pos,scr,tag)
        self.size=size
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def update(self,entitys):
        self.y+=self.fallspeed*entitys.dt
        self.pos=(self.x,self.y)
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
        screenw,screenh=pygame.display.get_window_size()
        if(((self.x<0)|(self.x>screenw))|((self.y<0)|(self.y>screenh))): self.kill()
    def apply(self,ent : Entity):
        pass
    def kill(self) -> None:
        super().kill()
    
        
