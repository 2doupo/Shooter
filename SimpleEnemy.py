from random import randint
from turtle import screensize
import pygame
from Enemy import Enemy
class SimpleEnemy(Enemy):
    size=30
    speed=1
    shotspeed=1.5
    image=pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/SimpleEnemy.png')
    cooldown=400
    last_shot_time=-100
    dir=1
    pv=100
    color=(255,0,0)
    def __init__(self,scr,pos=(0,0)):
        super().__init__(scr,self.cooldown,pos,self.speed,self.image,self.shotspeed)
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        

    def update(self,enemy_shots,player_shots,items):
        
        
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        self.x+=self.dir*self.speed
        self.pos=(self.x,self.y)
        
        super().update(enemy_shots,player_shots,items)
        
        #pygame.draw.circle(self.scr,self.color,self.pos,self.size/2)
        
        
