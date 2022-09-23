
from entity.Entity import EntInt
from entity.Player import Player
from entity.Enemy.Boss import Boss
from entity.Enemy.Malicious import Malicious
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.item.Shield import Shield
from entity.item.CadenceUp import CadUp
import pygame

class Level():
    
    def __init__(self,screen,screenw,screenh) -> None:
        self.bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
        self.entint=EntInt()
        self.screen=screen
        self.screenw=screenw
        self.screenh=screenh
        self.bossfight=False 
        Player(self.entint,scr=screen,pos=(screenw/2, screenh/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2))
        Player(self.entint,scr=screen,pos=(screenw/2, screenh/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g))
        maliciousnb=5
        for i in range(maliciousnb):
                Malicious(self.entint,screen,(screenw/2,50))
        SimpleEnemy(self.entint,screen,(screenw/2,50))

        shield=Shield(self.entint,(50,400),screen)
        CadUp(self.entint,(50,200),screen)
        self.clock=pygame.time.Clock()

    
    def start(self):
        pass
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
                win=self.bigarial.render("Victory !",False,(0,0,0))
                
                self.screen.blit(win,((self.screenw-win.get_width())/2,self.screenh/2))
        

    