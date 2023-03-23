
import pickle
class Savedata():
    totalkillcount=0
    best_Wave=0
    gold=0
    def __init__(self) -> None:
        pass
    def save(self):
        
        pickle.dump(self,open('Save/save.douteau','wb'))




