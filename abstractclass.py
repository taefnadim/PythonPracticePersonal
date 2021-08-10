from abc import ABC,abstractmethod

#Abstract Base Class, making object of this is not possible 
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

#Below class must have the printarea method defined
class rectangle(shape):
    def __init__(self):
        self.height=6
        self.width=7
    def printarea(self):
        return self.height*self.width


rect1=rectangle()
print(rect1.printarea())