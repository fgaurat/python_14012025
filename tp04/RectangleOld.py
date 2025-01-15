
class Rectangle:
    
    
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur

    def set_longueur(self,valeur):
        assert valeur>0        
        self.__longueur = valeur
    
    def set_largeur(self,valeur):
        assert valeur>0
        self.__largeur = valeur
        
    def get_surface(self):
        return self.__largeur*self.__longueur
    
    longueur = property(get_longueur,set_longueur,doc="longueur property")
    largeur = property(get_largeur,set_largeur,doc="largeur property")
    surface = property(get_surface,doc="surface property")