from Carre import Carre
from Cercle import Cercle
from typing import Protocol

class SurfaceAble(Protocol):

    @property 
    def test(self):
        pass
    
def show_surface(o:SurfaceAble):
    print(o.surface,type(o))
    
    
def main():
    c = Carre(5)
    ce = Cercle(5)
    print(c)
    show_surface(c)
    show_surface(ce)

if __name__=='__main__':
    main()
