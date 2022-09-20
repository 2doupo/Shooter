import pygame
from Item import Item
from Shot import Shot
from Entity import Entity,EntityTag
class Player(Entity):
    screenw,screenh=pygame.display.get_window_size()
    speed=0.5
    shotspeed=1.3
    cooldown=200
    last_shot_time=-100
    totalpv=100
    pv=100
    item_duration=5000
    buff : Item=None
    item_start=0
    image=pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/boat1.png'),(32,60))
    def __init__(self,entitys,pos=(0,0),scr : pygame.surface.Surface=None,key=None):
        super().__init__(entitys,pos,scr,EntityTag.PLAYER)
        self.key=key
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        

    def kill(self) -> None:
        super().kill()


    def update(self,entity):
        super().update(entity)
        if(self.pv<=0):
            self.kill()
        self.rect=pygame.Rect(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2,self.image.get_width(),self.image.get_height())
    
        if(pygame.key.get_pressed()[self.key[0]]):
            if(self.y+self.speed<self.screenh):
                self.y+=self.speed*entity.dt
                self.pos=(self.x,self.y)
        if(pygame.key.get_pressed()[self.key[1]]):
            if(self.y-self.speed>0):
                self.y+=-self.speed*entity.dt
                self.pos=(self.x,self.y)
        if(pygame.key.get_pressed()[self.key[2]]):
            if(self.x-self.speed>0):
                self.x+=-self.speed*entity.dt
                self.pos=(self.x,self.y)
        if(pygame.key.get_pressed()[self.key[3]]):
            if(self.x+self.speed<self.screenw):
                self.x+=self.speed*entity.dt
                self.pos=(self.x,self.y)
        if(pygame.key.get_pressed()[self.key[4]]&Player.endcooldown(self)):
            
            Shot(entity,(self.x,self.y-self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.PLAYERSHOT)
            self.last_shot_time=pygame.time.get_ticks()
        
        shot=pygame.sprite.spritecollide(self,entity.enemy_shots,True)
        if(len(shot)!=0):
            self.pv+=-10
        
        item: list[Item]=pygame.sprite.spritecollide(self,entity.items,True)
        if(len(item)!=0):
            for it in item:
                it.apply(self)
                if(self.buff==None):
                    
                    if(it.tag==EntityTag.CADUP):
                        self.buff=it
                else:
                    if(self.buff.tag==EntityTag.CADUP):
                        self.buff.stop(self)
                        self.buff=it
        if(self.buff!=None):
           
            if(self.buff.tag==EntityTag.CADUP):
                if(self.buff.end()):
                    self.buff.stop(self)
                    self.buff=None
        

        self.scr.blit(self.image,self.rect)
        pygame.draw.rect(self.scr,(0,0,0),pygame.Rect(self.x-self.image.get_width()/2,self.y+self.image.get_height(),self.image.get_width(),10))
        pygame.draw.rect(self.scr,(0,255,0),pygame.Rect(self.x-self.image.get_width()/2,self.y+self.image.get_height(),self.image.get_width()*self.pv/self.totalpv,10))
        #pygame.draw.rect(self.scr,(255,0,0),self.rect)
        

