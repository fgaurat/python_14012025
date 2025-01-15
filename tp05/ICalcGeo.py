from abc import ABCMeta,abstractmethod
# import abc
# Abstract Base Classe

class ICalcGeo( metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def surface(self)->float:
        # raise NotImplementedError()
        pass