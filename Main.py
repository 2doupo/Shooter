from os.path import exists #J'importe ce qu'il me faut pour le jeu. Il y a seulement pygame qui n'est pas de base sur python
import pickle
import pygame
pygame.init() # Initilisation de pygame
screenwidth=640 # Taille de l'écran en pixel
screenheight=800
screen = pygame.display.set_mode((screenwidth, screenheight),vsync=1) # création de l'écran avec la vsync d'activée (synchronisation verticale)

from Savedata import Savedata
from random import randint
from entity.item.CadenceUp import CadUp
from entity.item.DoubleShot import DShot # Importation de ce que j'ai besoin dans le Main que j'ai codé. 
from entity.item.Shield import Shield    # Attention à l'importation circulaire.(Si A importe B et B importe A python n'est pas content mais sur d'autre langage comme Java ça ne pose pas problème.)
from entity.Player import Player
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.Enemy.Malicious import Malicious
from entity.Enemy.Boss import Boss
from entity.Entity import EntInt,EntityTag
from Level import Level
from Menu import Menu

savedata=Savedata() #Création du stockage de la sauvegarde

if(exists('Save/save.douteau')): #Récupération des données de sauvegarde du fichier "save.douteau"
        savedata=pickle.load(open('Save/save.douteau','rb'))
else:
        pickle.dump(savedata,open('Save/save.douteau','wb'))
run = True
in_menu = True
in_level= False
level=Level(screen,screenwidth,screenheight,savedata)
menu=Menu(screen,screenwidth,screenheight)
water=pygame.image.load('Image/Watergreen.jpg')
w1=water.get_width()
w2=water.get_height()
scale=3.5
water=pygame.transform.scale(water,(w1*scale,w2*scale))
pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('Image/malicious.png'),(32,32)))
arial=pygame.font.Font('Font/arial.ttf',20)
bigarial=pygame.font.Font('Font/arial.ttf',100)
y=0
backspeed=0.5


while run: #la boucle du jeu qu'on appel souvent update. 
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        
        #Dessin de l'arrière plan
        y+=backspeed
        for i in range(int(screenwidth/water.get_width())+1):
                for j in range(-1,int(screenheight/water.get_height())+1):
                        screen.blit(water,(i*water.get_width(),(j*water.get_height()+y)%(screenheight+water.get_height())-water.get_height()))
        if(in_menu):
                menu.update()# mise à jour du menu
                
                if(menu.start_level):
                        in_level=True
                        in_menu=False
                        level.start()
        elif(in_level):
                level.update()# mise à jour du niveau

                
        pygame.display.update()# mise à jour de l'affichage de l'image
        
savedata.save() #Sauvegarde des données
pygame.quit() 
quit()