import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self,pos=(0,0),scr : pygame.surface.Surface=None) :
        super().__init__()
        self.pos=pos
        self.x=pos[0]
        self.y=pos[1]
        self.scr=scr

    def update(self):
        super().update(self)

