import pygame
from Entity import Entity
class Shot(Entity):
    screenw,screenh=pygame.display.get_window_size()
    def __init__(self,pos,scr,size,speed,team):
        super().__init__(pos,scr)
        self.size=size
        self.speed=speed
        self.team=team
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        


    def update(self,dt):
        
        
        if(self.team):
            self.y+=-self.speed*dt
            col=(255,255,0)
        else :
            self.y+=self.speed*dt
            col=(255,128,0)
        self.pos=(self.x,self.y)
        self.rect=pygame.Rect(self.x-self.size,self.y-self.size,2*self.size,2*self.size)
        if(((self.x<0)|(self.x>self.screenw))|((self.y<0)|(self.y>self.screenh))): self.kill()
        pygame.draw.circle(self.scr,col,self.pos,self.size)