
from turtle import st
from entity.Entity import EntInt
from entity.Player import Player
from entity.Enemy.Boss import Boss
from entity.Enemy.Malicious import Malicious
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.item.Shield import Shield
from entity.item.CadenceUp import CadUp
import pygame

class Level():
    wave=1
    def __init__(self,screen,screenw,screenh) -> None:
        self.bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
        self.arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
        self.entint=EntInt()
        self.screen=screen
        self.screenw=screenw
        self.screenh=screenh
        
        
        

    
    def start(self):
        self.clock=pygame.time.Clock()
        self.bossfight=False 
        
        simple_nb=3*self.wave
        malicious_nb=2*self.wave
        for i in range(malicious_nb):
                Malicious(self.entint,self.screen,(self.screenw/2,50))
        for i in range(simple_nb):
                SimpleEnemy(self.entint,self.screen,(self.screenw/2,50))



    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        dt = self.clock.tick(120)
        pygame.draw.rect(self.screen, (135,206,235), pygame.Rect(0,0,self.screenw, self.screenh))
        
        self.entint.update(dt)

        if(len(self.entint.players)==0):
                #run=False
                game_over=self.bigarial.render("Game Over",False,(0,0,0))
                
                self.screen.blit(game_over,((self.screenw-game_over.get_width())/2,self.screenh/2))

        if((self.entint.enemys.__len__()==0)& (not self.bossfight)):
                self.entint.add(Boss(self.entint,self.screen,(self.screenw/2,100)))
                self.bossfight=True
        elif((self.entint.enemys.__len__()==0)& (self.bossfight)):
                #run=False
                #win=self.bigarial.render("Victory !",False,(0,0,0))
                #self.screen.blit(win,((self.screenw-win.get_width())/2,self.screenh/2))
                self.wave+=1
                self.start()
        fps=self.arial.render("fps :" + str(int(self.clock.get_fps())),False,(0,0,0),(255,255,255))
        self.screen.blit(fps,(self.screenw-70,self.screenh-30))
        

    