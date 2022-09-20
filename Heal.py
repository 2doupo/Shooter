from Entity import EntityTag
from Item import Item
import pygame
from Player import Player
class Heal(Item):
    heal=50
    def __init__(self, pos=..., scr: pygame.surface.Surface = None, size=40):
        super().__init__(pos, scr, size,EntityTag.HEAL)

    def update(self,dt):
        super().update(dt)
        pygame.draw.rect(self.scr,(0,255,0),self.rect)
    def apply(self,pl : Player):
        super().apply()
        pl.pv=min(pl.totalpv,pl.pv+self.heal)
