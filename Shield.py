import pygame
from Item import Item
from Entity import Entity,EntityTag
class Shield(Item):
    size=40
    duration=5000
    start=None
    def __init__(self, entitys, pos=..., scr: pygame.surface.Surface = None):
        super().__init__(entitys, pos, scr, self.size, EntityTag.SHIELD)
    def end(self):
        return (pygame.time.get_ticks()-self.start)>self.duration

    def update(self, entitys):
        
        super().update(entitys)
        if(self.start!=None):
            
            if(self.end()):
                self.stop()
        pygame.draw.circle(self.scr,(0,0,255,100),self.pos,self.size/2)

    def apply(self,pl):
        super().apply(pl)
        self.pl=pl
        if(pl.buff!=None):
            pl.buff.stop()
        pl.buff=self
        self.start=pygame.time.get_ticks()

    def kill(self) -> None:
        return super().kill()
    def stop(self):
        self.pl.buff=None
        self.kill()

    