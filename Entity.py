import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self,entitys,pos=(0,0),scr : pygame.surface.Surface=None,tag=None) :
        super().__init__()
        self.pos=pos
        self.x=pos[0]
        self.y=pos[1]
        self.scr=scr
        self.tag=tag
        entitys.add(self)

    def kill(self) -> None:
        super().kill()


    def update(self,entitys):
        super().update(self)
    
class EntityTag():
        
    PLAYER=0
    
    #ENEMY=1
    SIMPLE_ENEMY=2
    MALICIOUS=3
    BOSS=4
    
    SHOT=5
    PLAYERSHOT=9
    ENEMYSHOT=10

    #ITEM=6
    CADUP=7
    HEAL=8

class EntInt():
  


    def __init__(self) -> None:
        self.entitys =pygame.sprite.Group()
        self.enemys =pygame.sprite.Group()
        self.players =pygame.sprite.Group()
        self.items =pygame.sprite.Group()
        self.shots =pygame.sprite.Group()
        self.player_shots  =pygame.sprite.Group()
        self.enemy_shots  =pygame.sprite.Group()
    def add(self,ent : Entity) -> None:
        self.entitys.add(ent)
        if(ent.tag==EntityTag.PLAYER):
            self.players.add(ent)
        elif(ent.tag in ([EntityTag.SIMPLE_ENEMY,EntityTag.MALICIOUS,EntityTag.BOSS])):
            self.enemys.add(ent)
        elif(ent.tag in [EntityTag.CADUP,EntityTag.HEAL]):
            self.items.add(ent)
        elif(ent.tag==EntityTag.PLAYERSHOT):
            self.player_shots.add(ent)
        elif(ent.tag==EntityTag.ENEMYSHOT):     
            self.enemy_shots.add(ent)
    def remove(self,ent) -> None:
        self.entitys.remove(ent)
        if(ent.tag==EntityTag.PLAYER):
            self.players.remove(ent)
        elif(ent.tag in ([EntityTag.SIMPLE_ENEMY,EntityTag.MALICIOUS,EntityTag.BOSS])):
            self.enemys.remove(ent)
        elif(ent.tag in [EntityTag.CADUP,EntityTag.HEAL]):
            self.items.remove(ent)
        elif(ent.tag==EntityTag.SHOT):
            #print(ent.tag)
            if(ent.team):
                self.player_shots.remove(ent)
            else: self.enemy_shots.remove(ent)
    def update(self,dt):
        self.dt=dt
        self.entitys.update(self)
        

