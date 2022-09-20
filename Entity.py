import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self,pos=(0,0),scr : pygame.surface.Surface=None,tag=None) :
        super().__init__()
        self.pos=pos
        self.x=pos[0]
        self.y=pos[1]
        self.scr=scr
        self.tag=tag

    def update(self):
        super().update(self)
    
class EntityTag():
        
    PLAYER=0
    
    #ENEMY=1
    SIMPLE_ENEMY=2
    MALICIOUS=3
    BOSS=4
    
    SHOT=5

    #ITEM=6
    CADUP=7
    HEAL=8


