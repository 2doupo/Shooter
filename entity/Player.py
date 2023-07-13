import pygame
from entity.item.Item import Item
from entity.Shot import Shot
from entity.Entity import Entity,EntityTag
class Player(Entity):
    
    speed=0.5
    shotspeed=1.3
    cooldown=200
    last_shot_time=-100
    totalpv=100
    pv=100
    
    image=pygame.transform.scale(pygame.image.load('Image/boat1.png'),(32,60))
    def __init__(self,entitys,pos=(0,0),scr : pygame.surface.Surface=None,key=None):
        super().__init__(entitys,pos,scr,EntityTag.PLAYER)
        self.screenw,self.screenh=pygame.display.get_window_size()
        self.buffs : list[Item]=[]
        self.bufftags : list[EntityTag]=[]
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
        if(pygame.key.get_pressed()[self.key[1]]):
            if(self.y-self.speed>0):
                self.y-=self.speed*entity.dt
        if(pygame.key.get_pressed()[self.key[2]]):
            if(self.x-self.speed>0):
                self.x+=-self.speed*entity.dt
        if(pygame.key.get_pressed()[self.key[3]]):
            if(self.x+self.speed<self.screenw):
                self.x+=self.speed*entity.dt
        if(pygame.key.get_pressed()[self.key[4]]&Player.endcooldown(self)):
            if(len(self.buffs)!=0):
                
                if(EntityTag.DSHOT in self.bufftags):
                    Shot(entity,(self.x-self.image.get_width()/2,self.y-self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.PLAYERSHOT)   
                    Shot(entity,(self.x+self.image.get_width()/2,self.y-self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.PLAYERSHOT)
                else:
                    Shot(entity,(self.x,self.y-self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.PLAYERSHOT)

            else: 
                Shot(entity,(self.x,self.y-self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.PLAYERSHOT)
            self.last_shot_time=pygame.time.get_ticks()
        self.pos=(self.x, self.y)
        shot=pygame.sprite.spritecollide(self,entity.enemy_shots,True)
        if(len(shot)!=0):
            if(len(self.buffs)!=0):
                if(EntityTag.SHIELD in self.buffs):
                    self.pv-=10
            else:
                self.pv-=10
        enemy=pygame.sprite.spritecollide(self,entity.enemys,False)
        if(len(enemy)!=0):
            self.pv-=0.5
        item: list[Item]=pygame.sprite.spritecollide(self,entity.items,True)
        if(len(item)!=0):
            for it in item:
                it.apply(self)
        
            
        
        self.scr.blit(self.image,self.rect)
        if(len(self.buffs)!=0):
            for buff in self.buffs:
                if(buff!=None):
                    if(buff.end()):
                        buff.stop()
        if(len(self.buffs)!=0):
            if(EntityTag.SHIELD in self.bufftags):
                pygame.draw.circle(self.scr,(0,0,255,2),self.pos,40)

        pygame.draw.rect(self.scr,(0,0,0),pygame.Rect(self.x-self.image.get_width()/2,self.y+self.image.get_height(),self.image.get_width(),10))
        pygame.draw.rect(self.scr,(0,255,0),pygame.Rect(self.x-self.image.get_width()/2,self.y+self.image.get_height(),self.image.get_width()*self.pv/self.totalpv,10))
        #pygame.draw.rect(self.scr,(255,0,0),self.rect)
        

