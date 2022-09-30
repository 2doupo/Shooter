from entity.Enemy.Enemy import Enemy
import pygame
from entity.Shot import Shot
from entity.Entity import EntityTag
class Boss(Enemy):
    image=pygame.transform.scale(pygame.image.load('Image/SimpleEnemy.png'),(26*5,32*5))
    speed=0.25
    shotspeed=0.7
    cooldown=100
    last_shot_time=-100
    dir=1
    pv=500
    color=(0,0,0)
    nb_shot=0
    def __init__(self,entitys,scr,pos=(0,0)):
        super().__init__(entitys,scr,self.cooldown,pos,self.speed,self.image,self.shotspeed,EntityTag.BOSS)
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        

    def kill(self,entitys) -> None:
        super().kill(entitys)
    def update(self,entitys):
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        

        self.x+=self.dir*self.speed*entitys.dt
        self.pos=(self.x,self.y)

        if(self.endcooldown()):
            if(self.nb_shot!=0):
                Shot(entitys,(self.x,self.y+self.image.get_height()/2),self.scr,5,self.shotspeed,EntityTag.ENEMYSHOT)
                
            self.last_shot_time=pygame.time.get_ticks()
            self.nb_shot=(self.nb_shot+1)%10
        super().update(entitys)
        