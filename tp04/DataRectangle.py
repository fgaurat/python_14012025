from dataclasses import dataclass
from typing import ClassVar
@dataclass
class DataRectangle:
    longueur:int=1
    largeur:int=1
    counter: ClassVar[int] = 0
    
    def __post_init__(self):
        DataRectangle.counter+=1
   
    @property
    def surface(self):
        return self.longueur*self.largeur
    
    def __del__(self):
        print("def __del__(self)")