from Entity import Entity
import pygame

class Item(Entity):
    fallspeed=0.25
    def __init__(self,entitys,pos=(0,0),scr : pygame.surface.Surface=None,size=40,tag=None):
        super().__init__(entitys,pos,scr,tag)
        self.size=size
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def update(self,entitys):
        self.y+=self.fallspeed*entitys.dt
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def apply(ent : Entity):
        pass
    def kill(self) -> None:
        super().kill()
    
        
