from random import randint
import pygame
pygame.init()
screenwidth=640
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight))
from Heal import Heal
from Player import Player
from Enemy import Enemy
from Entity import Entity
from SimpleEnemy import SimpleEnemy
from Malicious import Malicious
from Boss import Boss
from Item import Item,Itemtag
from ShotFactory import ShotFactory
from CadenceUp import CadUp


pygame.init()


pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('C:/Users/Arthur/Desktop/game/Test/Image/malicious.png'),(32,32)))
arial=pygame.font.Font('C:/Windows/Fonts/arial.ttf',20)



bossfight=False 
players=pygame.sprite.Group()
players.add(Player(scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2)))
players.add(Player(scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_s,pygame.K_z,pygame.K_q,pygame.K_d,pygame.K_g)))
#players.add(Player(scr=screen,pos=(screenwidth/2, screenheight/2),key=(pygame.K_k,pygame.K_i,pygame.K_j,pygame.K_l,pygame.K_m)))


enemys =pygame.sprite.Group()
maliciousnb=5
for i in range(maliciousnb):
        enemys.add(Malicious(screen,(screenwidth/2,50)))
enemys.add(SimpleEnemy(screen,(screenwidth/2,50)))

players_shots=pygame.sprite.Group()
enemys_shots=pygame.sprite.Group()
clock=pygame.time.Clock()

items=pygame.sprite.Group()
items.add(CadUp((50,400),screen))
items.add(CadUp((50,200),screen))

run = True
while run:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.rect(screen, (135,206,235), pygame.Rect(0,0,screenwidth, screenheight))
        
        players.update(players_shots,enemys_shots,items)
        enemys.update(enemys_shots,players_shots,items) 
        enemys_shots.update()
        players_shots.update()
        items.update()

        if(len(players)==0):
                run=False
        for player in players:
                if(player.pv<=0):
                        #run=False
                        player.kill()

        if((enemys.__len__()==0)& (not bossfight)):
                enemys.add(Boss(screen,(screenwidth/2,0)))
                bossfight=True
        elif((enemys.__len__()==0)& (bossfight)):
                run=False
        fps=arial.render("fps :" + str(int(clock.get_fps())),False,(0,0,0),(255,255,255))
        screen.blit(fps,(screenwidth-70,screenheight-30))
        
        #print(clock.get_time())
        t=clock.get_time()
        
        if(t<17):
                pygame.time.wait(17-t)
        #ms_par_frame=arial.render(str(clock.get_time()),False,(0,0,0))
        #screen.blit(ms_par_frame,(screenwidth-60,screenheight-60))
        pygame.display.update()
        



        

pygame.quit() 
quit()