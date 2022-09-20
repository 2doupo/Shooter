from Item import Item,Itemtag
import pygame
from Player import Player
class CadUp(Item):
    size=40
    duration=5000
    taken=False
    start=0
    def __init__(self, pos=..., scr: pygame.surface.Surface = None):
        super().__init__(Itemtag.CAD,pos, scr,self.size)

    def end(self):
        return pygame.time.get_ticks()-self.start>self.duration
    def update(self):
        super().update()
        pygame.draw.rect(self.scr,(255,255,0),self.rect)

    def apply(self,pl : Player):
        super().apply()
        pl.cooldown*=1/2
        self.start=pygame.time.get_ticks()
        self.taken=True
    def stop(self,pl : Player):
        pl.cooldown*=2
        self.kill()
        


        

    