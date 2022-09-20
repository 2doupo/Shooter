from Entity import Entity
import pygame

class Item(Entity):
    fallspeed=0.25
    def __init__(self,pos=(0,0),scr : pygame.surface.Surface=None,size=40,tag=None):
        super().__init__(pos,scr,tag)
        self.size=size
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def update(self,dt):
        self.y+=self.fallspeed*dt
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def apply(ent : Entity):
        pass
    
        
