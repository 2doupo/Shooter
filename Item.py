from Entity import Entity
import pygame
class Itemtag:
    CAD=0
    Heal=1
class Item(Entity):
    fallspeed=0.25
    def __init__(self,tag: Itemtag,pos=(0,0),scr : pygame.surface.Surface=None,size=40):
        super().__init__(pos,scr)
        self.size=size
        self.tag=tag
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def update(self,dt):
        self.y+=self.fallspeed*dt
        self.rect=pygame.Rect(self.x-self.size/2,self.y-self.size/2,self.size,self.size)
    def apply(ent : Entity):
        pass
    
        
