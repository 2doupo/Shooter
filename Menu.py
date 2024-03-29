import pygame

class Button():
        START=0
        LEVELS=1
        ENDLESS=2
        OPTIONS=3
        QUIT=4

class Menu():

    button_number=Button.QUIT+1
    last_up_pressed=False
    last_down_pressed=False
    start_level=False
    start_endless=False
    in_options=False
    end=False
    def __init__(self,screen,screenw,screenh) -> None:
        self.arial=pygame.font.Font('Font/arial.ttf',40)
        self.clock=pygame.time.Clock()
        self.screen=screen
        self.screenw=screenw
        self.screenh=screenh
        self.start=self.arial.render("Start",False,(0,0,0),(255,255,255))
        self.levels=self.arial.render("Levels",False,(0,0,0),(255,255,255))
        self.options=self.arial.render("Options",False,(0,0,0),(255,255,255))
        self.quit=self.arial.render("Quit",False,(0,0,0),(255,255,255))
        self.endlessmode=self.arial.render("Endless Mode",False,(0,0,0),(255,255,255))
        self.selected_button=Button.START


    def get_button_rect(self):
     
        match self.selected_button :
            
            case Button.START: 

                return self.start.get_rect().move((self.screenw-self.start.get_width())/2,self.screenh*(self.selected_button+1)/(self.button_number+1))
            
            case Button.LEVELS : 
                return self.levels.get_rect().move((self.screenw-self.levels.get_width())/2,self.screenh*(self.selected_button+1)/(self.button_number+1))
            case Button.OPTIONS: 
                return self.options.get_rect().move((self.screenw-self.options.get_width())/2,self.screenh*(self.selected_button+1)/(self.button_number+1))
            case Button.QUIT : 
                return self.quit.get_rect().move((self.screenw-self.quit.get_width())/2,self.screenh*(self.selected_button+1)/(self.button_number+1))
            case Button.ENDLESS:
                return self.endlessmode.get_rect().move((self.screenw-self.endlessmode.get_width())/2,self.screenh*(self.selected_button+1)/(self.button_number+1))



    def clic(self):
        match self.selected_button :
            case Button.START: 
                self.start_level=True
            case Button.LEVELS : 
                pass
            case Button.ENDLESS:
                self.start_endless=True
            case Button.OPTIONS: 
                self.in_options=True
            case Button.QUIT : 
                self.end=True
                


                
    


    def menu_update(self):
        if((not pygame.key.get_pressed()[pygame.K_UP]) & self.last_up_pressed):

            self.selected_button=(self.selected_button-1)%self.button_number
        if((not pygame.key.get_pressed()[pygame.K_DOWN]) & self.last_down_pressed):
            self.selected_button=(self.selected_button+1)%self.button_number
        
        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            self.clic()

        
        self.last_up_pressed=pygame.key.get_pressed()[pygame.K_UP]
        self.last_down_pressed=pygame.key.get_pressed()[pygame.K_DOWN]

        #pygame.draw.rect(self.screen, (135,206,235), pygame.Rect(0,0,self.screenw, self.screenh))
        
        
        self.screen.blit(self.start,((self.screenw-self.start.get_width())/2,self.screenh/(self.button_number+1)))
        self.screen.blit(self.levels,((self.screenw-self.levels.get_width())/2,2*self.screenh/(self.button_number+1)))
        self.screen.blit(self.endlessmode,((self.screenw-self.endlessmode.get_width())/2,3*self.screenh/(self.button_number+1)))
        self.screen.blit(self.options,((self.screenw-self.options.get_width())/2,4*self.screenh/(self.button_number+1)))
        self.screen.blit(self.quit,((self.screenw-self.quit.get_width())/2,5*self.screenh/(self.button_number+1)))
        

        #selected=self.arial.render("selected :" + str(self.selected_button),False,(0,0,0),(255,255,255))
        #self.screen.blit(selected,(self.screenw-selected.get_width(),self.screenh-50))

        pygame.draw.rect(self.screen,(0,0,0),self.get_button_rect(),2)
        
    def options_update(self):
            pass

    def update(self):
        dt = self.clock.tick(120)
        
        if(not self.in_options):
            self.menu_update()
        else:
            self.options_update()
    
        
        




    


        
        


    
    

