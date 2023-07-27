from os.path import exists #J'importe ce qu'il me faut pour le jeu. Il y a seulement pygame qui n'est pas de base sur python
import pickle
import pygame

from Savedata import Savedata
from random import randint
from entity.item.CadenceUp import CadUp
from entity.item.DoubleShot import DShot # Importation de ce que j'ai besoin dans Game que j'ai codé. 
from entity.item.Shield import Shield    # Attention à l'importation circulaire.(Si A importe B et B importe A python n'est pas content mais sur d'autre langage comme Java ça ne pose pas problème.)
from entity.Player import Player
from entity.Enemy.SimpleEnemy import SimpleEnemy
from entity.Enemy.Malicious import Malicious
from entity.Enemy.Boss import Boss
from entity.Entity import EntInt,EntityTag
from Endless import Endless
from Menu import Menu
from Levels.Level import Level
class Game:
    level=None
    def __init__(self) -> None:
        pygame.init() # Initilisation de pygame
        self.screenwidth=640 # Taille de l'écran en pixel
        self.screenheight=800
        self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight),vsync=1) # création de l'écran avec la vsync d'activée (synchronisation verticale)
        self.savedata=Savedata() #Création du stockage de la sauvegarde
        if(exists('Save/save.douteau')): #Récupération des données de sauvegarde du fichier "save.douteau"
            self.savedata=pickle.load(open('Save/save.douteau','rb'))
        else:
            pickle.dump(self.savedata,open('Save/save.douteau','wb'))
        self.run = True #Variable qui dit quand le jeu est en cours
        self.in_menu = True #Variable qui dit quand on est dans le menu
        self.in_level= False #Variable qui dit quand on est dans un niveau
        self.in_endless=False
        self.endless=Endless(self.screen,self.screenwidth,self.screenheight,self.savedata) #Création du niveau
      
        
        self.menu=Menu(self.screen,self.screenwidth,self.screenheight) #Création du Menu
        water=pygame.image.load('Image/Watergreen.jpg')#Image du fond de l'écran
        w1=water.get_width()
        w2=water.get_height()
        scale=3.5
        self.water=pygame.transform.scale(water,(w1*scale,w2*scale))#Je calibre la taille de cette image
        pygame.display.set_caption("Test")
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load('Image/malicious.png'),(32,32)))#Petite icône de la fenêtre
        arial=pygame.font.Font('Font/arial.ttf',20) # Chargement des polices
        bigarial=pygame.font.Font('Font/arial.ttf',100)
        self.y=0 #position du fond d'écran
        self.backspeed=0.5 #vitesse de défilement du fond d'écran
        self.selected_level=1
    
    #Fonction de mise à jour du jeu
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.run = False
        
        #Dessin de l'arrière plan
        self.y+=self.backspeed
        for i in range(int(self.screenwidth/self.water.get_width())+1):
                for j in range(-1,int(self.screenheight/self.water.get_height())+1):
                        self.screen.blit(self.water,(i*self.water.get_width(),(j*self.water.get_height()+self.y)%(self.screenheight+self.water.get_height())-self.water.get_height()))
        if(self.in_menu):
                self.menu.update()# mise à jour du menu
                
                if(self.menu.start_level):
                        self.in_level=True
                        self.in_menu=False
                        self.level=Level(self.screen,self.screenwidth,self.screenheight,self.savedata,self.selected_level) #start selected level
                        self.level.start()
                if(self.menu.start_endless):
                    self.in_endless=True
                    self.in_menu=False
                    self.endless.start()
                      
                

                      
                    

        elif(self.in_endless):
            self.endless.update()# mise à jour du niveau
        elif(self.in_level):
             self.level.update()

                
        pygame.display.update()# mise à jour de l'affichage de l'image     
        
    def quit(self):
        self.savedata.save() #Sauvegarde des données
        pygame.quit() 
        quit()

