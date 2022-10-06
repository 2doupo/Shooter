from entity.Entity import EntityTag
from entity.item.Item import Item
import pygame

class CadUp(Item):
    size=40
    duration=5000
    start=None
    def __init__(self,entitys, pos=..., scr: pygame.surface.Surface = None):
        super().__init__(entitys,pos, scr,self.size,EntityTag.CADUP)

    def end(self):
        return pygame.time.get_ticks()-self.start>self.duration
    def update(self,entitys):
        super().update(entitys)
        pygame.draw.rect(self.scr,(255,255,0),self.rect)
    
    def apply(self,pl):
        super().apply(pl)
        self.pl=pl
        
        pl.buffs.append(self)
        pl.bufftags.append(self.tag)
        pl.cooldown*=1/2
        self.start=pygame.time.get_ticks()
    def stop(self):
        self.pl.buffs.remove(self)
        self.pl.bufftags.remove(self.tag)
        self.pl.cooldown*=2
        self.kill()
    def kill(self) -> None:
        super().kill()
        


        

    