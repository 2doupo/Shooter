class Upgrade_tag:
        DAMAGE=1
        CADENCE=2
        SHOT_SPEED=3
        SPEED=4
        HEALTH=5
        REGEN=6
        #DRONE
        #LASER 




class Upgrade:

    
    def __init__(self,tag : Upgrade_tag) -> None:
        self.tag=tag

    def choose(self,player) -> None :
         pass