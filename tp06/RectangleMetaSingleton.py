class SingletonMeta(type):
    
    instance = None
    
    def __call__(self,*args,**kwargs):
        if self.instance is None:
            print("call")
            self.instance = super().__call__(*args,**kwargs)
        else:
            print("init")
            self.instance.__init__(*args,**kwargs)
        
        return self.instance

class RectangleMetaSingleton(metaclass=SingletonMeta):

    __cpt = 0

    __slots__ = ("__longueur", "__largeur")

    def __init__(self, longueur=1, largeur=1):
        print(f"def __init__(self, {longueur}, {largeur})")
        self.__longueur = longueur
        self.__largeur = largeur

        RectangleMetaSingleton.__cpt += 1

    @classmethod
    def buildFromStr(cls, value):

        longueur, largeur = [int(v) for v in value.split(";")]

        return cls(longueur, largeur)

    @property
    def longueur(self):
        return self.__longueur

    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self, valeur):

        assert valeur > 0

        self.__longueur = valeur

    @largeur.setter
    def largeur(self, valeur):
        assert valeur > 0
        self.__largeur = valeur

    @staticmethod
    def get_cpt():
        return RectangleMetaSingleton.__cpt

    @property
    def surface(self):

        return self.__largeur*self.__longueur

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.longueur=},{self.largeur=}"

    def __eq__(self, value) -> bool:
        return self.longueur == value.longueur and self.largeur == value.largeur
