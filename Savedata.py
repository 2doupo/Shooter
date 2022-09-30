
import pickle
class Savedata():
    killcount=0
    def __init__(self) -> None:
        pass
    def save(self):
        
        pickle.dump(self,open('Save/save.douteau','wb'))




