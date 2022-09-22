import pygame
from Item import Item
from Entity import EntityTag
class DShot(Item):
    start=None
    duration = 5000
    def __init__(self, entitys, pos=..., scr: pygame.surface.Surface = None, size=40):
        super().__init__(entitys, pos, scr, size, EntityTag.DSHOT)

    def end(self):
        return pygame.time.get_ticks()-self.start>self.duration
    def update(self,entitys):
        super().update(entitys)
        if(self.start!=None):
            if(self.end()):
                self.stop()
        pygame.draw.rect(self.scr,(255,127,0),self.rect)
    
    def apply(self,pl):
        super().apply()
        self.pl=pl
        if(pl.buff!=None):
            pl.buff.stop()
        pl.buff=self
        self.start=pygame.time.get_ticks()
    def stop(self):
        self.pl.buff=None
        self.kill()
    def kill(self) -> None:
        super().kill()