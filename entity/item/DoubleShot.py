import pygame
from entity.item.Item import Item
from entity.Entity import EntityTag
class DShot(Item):
    size=40
    duration=5000
    start=None
    def __init__(self, entitys, pos=..., scr: pygame.surface.Surface = None):
        super().__init__(entitys, pos, scr, self.size, EntityTag.DSHOT)

    def end(self):
        return pygame.time.get_ticks()-self.start>self.duration
    def update(self,entitys):
        super().update(entitys)
        if(self.start!=None):
            if(self.end()):
                self.stop()
        pygame.draw.rect(self.scr,(255,127,0),self.rect)
    
    def apply(self,pl):
        super().apply(pl)
        self.pl=pl
        pl.buffs.append(self)
        pl.bufftags.append(self.tag)
        self.start=pygame.time.get_ticks()
    def stop(self):
        self.pl.buffs.remove(self)
        self.pl.bufftags.remove(self.tag)
        self.kill()
    def kill(self) -> None:
        super().kill()