import pygame
from Entity import Entity,EntityTag
from Enemy import Enemy
from Player import Player
from Item import Item
from Shot import Shot
class EntInt():
    entitys : list[Entity]=[]
    enemys : list[Enemy]=[]
    players : list[Player]=[]
    items : list[Item]=[]
    shots : list[Shot]=[]
    player_shots : list[Shot]=[]
    enemy_shots : list[Shot]=[]


    def __init__(self) -> None:
        pass
    def add(self,ent : Entity) -> None:
        self.enemys.append(ent)
        if(ent.tag==EntityTag.PLAYER):
            self.players.append(ent)
        elif(ent.tag in ([EntityTag.SIMPLE_ENEMY,EntityTag.MALICIOUS,EntityTag.BOSS])):
            self.enemys.append(ent)
        elif(ent.tag in [EntityTag.SHOT,EntityTag.CADUP,EntityTag.HEAL]):
            self.items.append(ent)
        elif(ent.tag==EntityTag.SHOT):
            if(ent.team==True):
                self.player_shots.append(ent)
            else: self.enemy_shots.append(ent)
    

    def update(self,dt):
        for ent in self.entitys:
            if(ent.tag==EntityTag.PLAYER):
                ent.update(self.player_shots,self.enemy_shots,self.items,dt)
            elif(ent.tag in ([EntityTag.SIMPLE_ENEMY,EntityTag.MALICIOUS,EntityTag.BOSS])):
                ent.update(self.enemy_shots,self.player_shots,self.items,dt)
            elif(ent.tag in [EntityTag.SHOT,EntityTag.CADUP,EntityTag.HEAL]):
                ent.update(dt)
            
