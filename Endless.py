
from random import randint
from Savedata import Savedata
from entity.Entity import EntInt
from entity.Player import Player
from entity.Enemy.Boss import Boss
from entity.Enemy.Malicious import Malicious
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.item.Shield import Shield
from entity.item.CadenceUp import CadUp
import pygame

class Endless():
        wave=1
        def __init__(self,screen,screenw,screenh,savedata : Savedata) -> None:
                self.bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
                self.arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
                self.entint=EntInt()
                self.screen=screen
                self.screenw=screenw
                self.screenh=screenh
                self.savedata=savedata
                self.entint.killcount=0
                self.best_wave=savedata.best_Wave
                self.nb_player=1

                
                
                

        
        def start(self):
                if(self.entint.players.__len__()==0):
                        Player(self.entint,scr=self.screen,pos=(self.screenw/2, self.screenh/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g))

                        if(self.nb_player==2):
                                Player(self.entint,scr=self.screen,pos=(self.screenw/2, self.screenh/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2))

                self.clock=pygame.time.Clock()
                self.bossfight=False 
                
                simple_nb=0*self.wave
                malicious_nb=5*self.wave
                for i in range(malicious_nb):
                        Malicious(self.entint,self.screen,(randint(0,self.screenw-1),50))
                for i in range(simple_nb):
                        SimpleEnemy(self.entint,self.screen,(randint(0,self.screenw-1),50))


        def update(self):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                dt = self.clock.tick(120)
                #pygame.draw.rect(self.screen, (135,206,235), pygame.Rect(0,0,self.screenw, self.screenh))
                
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
                        self.best_wave=max(self.wave,self.best_wave)
                        self.start()
        
                self.info_print()


                if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
                        print(self.entint.killcount)
                        self.savedata.totalkillcount+=self.entint.killcount
                        self.savedata.best_Wave=self.best_wave
                        self.savedata.save()
                        pygame.quit() 
                        quit()
                #print(self.entint.players.sprites()[0].buffs,self.entint.players.sprites()[1].buffs)
                #print(len(self.entint.items))
        def info_print(self):
                fps=self.arial.render("fps :" + str(int(self.clock.get_fps())),False,(0,0,0),(255,255,255))
                self.screen.blit(fps,(self.screenw-70,self.screenh-30))

                kc=self.arial.render("killcount :" + str(self.entint.killcount),False,(0,0,0),(255,255,255))
                self.screen.blit(kc,(0,self.screenh-30))

                bw=self.arial.render("bestwave :" + str(self.best_wave),False,(0,0,0),(255,255,255))
                self.screen.blit(bw,(0,self.screenh-60))

                w=self.arial.render("wave :" + str(self.wave),False,(0,0,0),(255,255,255))
                self.screen.blit(w,(0,self.screenh-90))
      
        
        

    