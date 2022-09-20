from Item import Item,Itemtag
import pygame
from Player import Player
class Heal(Item):
    heal=50
    def __init__(self, pos=..., scr: pygame.surface.Surface = None, size=40):
        super().__init__(Itemtag.Heal, pos, scr, size)

    def update(self,dt):
        super().update(dt)
        pygame.draw.rect(self.scr,(0,255,0),self.rect)
    def apply(self,pl : Player):
        super().apply()
        pl.pv=min(pl.totalpv,pl.pv+self.heal)
