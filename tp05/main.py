from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print("cote",c.cote)
    print("surface",c.surface)
    c.cote = 5
    print("cote",c.cote)
    print("surface",c.surface)    
    
    print(c)
    print(50*'-')
    ce = Cercle(12)
    print(ce.surface)
if __name__=='__main__':
    main()
