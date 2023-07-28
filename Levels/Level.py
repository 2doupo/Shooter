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

class Level():
        enemy=[]
        end=False
        def __init__(self,screen,screenw,screenh,savedata : Savedata, level_number) -> None:
                self.bigarial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',100)
                self.arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)
                self.entint=EntInt()
                self.screen=screen
                self.screenw=screenw
                self.screenh=screenh
                self.savedata=savedata
                self.entint.killcount=0
                self.nb_player=1
                self.number=level_number
                self.waves=self.get_waves()
                self.current_wave=-1
                self.win=False
                self.pre_next=False
                self.next=False
                self.cooldown_until_next=1000
                self.start_cooldown=0
                
        def spawn_enemys_in_wave(self,wave : str):
                for i in range(len(wave)//2):
                        nb=int(wave[2*i])
                        type=wave[2*i+1]
                        if(type=='R'):
                                for j in range(nb):
                                        SimpleEnemy(self.entint,self.screen,(randint(0,self.screenw-1),50))
                        elif(type=='M'):
                                for j in range(nb):
                                        Malicious(self.entint,self.screen,(randint(0,self.screenw-1),50))
                        elif(type=='B'):
                                for j in range(nb):
                                        Boss(self.entint,self.screen,(randint(0,self.screenw-1),50))
                        
                        

                        

        def get_waves(self):
                text=open("Levels/"+str(self.number)+".txt")
                content=text.read()
                return content.split('/')
                
                
                

        
        def start(self):
                if(self.entint.players.__len__()==0):
                        Player(self.entint,scr=self.screen,pos=(self.screenw/2, self.screenh/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g))

                        if(self.nb_player==2):
                                Player(self.entint,scr=self.screen,pos=(self.screenw/2, self.screenh/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2))

                self.clock=pygame.time.Clock()
                

                



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
                
                if((len(self.entint.enemys)==0)&(self.current_wave<len(self.waves))):
                        self.current_wave+=1
                        if(self.current_wave>=len(self.waves)):
                                self.win=True
                        else:
                                self.spawn_enemys_in_wave(self.waves[self.current_wave])
                        
                        
                        

                        
                if(self.win):
                        level_cleared=self.bigarial.render("Level Cleared",False,(0,0,0))
                        self.screen.blit(level_cleared,((self.screenw-level_cleared.get_width())/2,self.screenh/2))
                        if(not self.pre_next):
                                
                                
                                self.start_cooldown=pygame.time.get_ticks()
                                self.pre_next=True
                        else:

                                if(pygame.time.get_ticks()-self.start_cooldown>self.cooldown_until_next):
                                        self.next=True
                                        
 


                self.info_print()


                if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
                        #print(self.entint.killcount)
                        self.savedata.totalkillcount+=self.entint.killcount
                        self.savedata.save()
                        self.end=True
                         
                
                #print(self.entint.players.sprites()[0].buffs,self.entint.players.sprites()[1].buffs)
                #print(len(self.entint.items))
        def info_print(self):
                fps=self.arial.render("fps :" + str(int(self.clock.get_fps())),False,(0,0,0),(255,255,255))
                self.screen.blit(fps,(self.screenw-70,self.screenh-30))

                kc=self.arial.render("killcount :" + str(self.entint.killcount),False,(0,0,0),(255,255,255))
                self.screen.blit(kc,(0,self.screenh-30))

        
                


        
        

    
