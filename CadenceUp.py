from Entity import EntityTag
from Item import Item
import pygame

class CadUp(Item):
    size=40
    duration=5000
    taken=False
    start=0
    def __init__(self,entitys, pos=..., scr: pygame.surface.Surface = None):
        super().__init__(entitys,pos, scr,self.size,EntityTag.CADUP)

    def end(self):
        return pygame.time.get_ticks()-self.start>self.duration
    def update(self,entitys):
        super().update(entitys)
        pygame.draw.rect(self.scr,(255,255,0),self.rect)
    
    def apply(self,pl):
        super().apply()
        pl.cooldown*=1/2
        self.start=pygame.time.get_ticks()
        self.taken=True
    def stop(self,pl):
        pl.cooldown*=2
        self.kill()
    def kill(self) -> None:
        super().kill()
        


        

    