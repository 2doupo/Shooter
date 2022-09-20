from Enemy import Enemy
import pygame
class Boss(Enemy):
    image=pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/SimpleEnemy.png'),(26*5,32*5))
    speed=0.25
    shotspeed=0.7
    cooldown=100
    last_shot_time=-100
    dir=1
    pv=500
    color=(0,0,0)
    def __init__(self,scr,pos=(0,0)):
        super().__init__(scr,self.cooldown,pos,self.speed,self.image,self.shotspeed)
    
    def endcooldown(self):
        return pygame.time.get_ticks()-self.last_shot_time>self.cooldown
        

    def update(self,enemy_shots,player_shots,items,dt):
        
        if((self.x>pygame.display.get_window_size()[0])|(0>self.x)):
            self.dir*=-1
            #print("change dir")
        

        self.x+=self.dir*self.speed*dt
        self.pos=(self.x,self.y)

        super().update(enemy_shots,player_shots,items,dt)
        