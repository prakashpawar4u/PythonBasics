

#from abc import ABC, abstractclassmethod
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__ (self):
        print("Area Constructor")

    @abstractmethod
    def area(self):
        print("In Area Method")
        pass
    @abstractmethod
    def perimeter(self):
        print("In Perimeter Method")
        pass

class Square(Shape):
    def __init__(self,side):
        print("Square Constructor")
        self.__side = side
    #implement all the abstract method in sub class which is inheriting the ABSTRACT CLASS
    def area(self):
        print("Area in Square")
        return self.__side * self.__side

    def perimeter(self):
        print("Perimeter in Square")
        return 4 * self.__side

# shape = Shape()
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

sq = Square(5)
print(sq.area())
print(sq.perimeter())