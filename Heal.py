from Entity import EntityTag
from Item import Item
import pygame
import Player
class Heal(Item):
    heal=50
    def __init__(self, entitys,pos=..., scr: pygame.surface.Surface = None, size=40):
        super().__init__(entitys,pos, scr, size,EntityTag.HEAL)

    def update(self,entitys):
        super().update(entitys)
        pygame.draw.rect(self.scr,(0,255,0),self.rect)
    def apply(self,pl):
        super().apply()
        pl.pv=min(pl.totalpv,pl.pv+self.heal)
        self.kill()
    def kill(self) -> None:
        super().kill()
