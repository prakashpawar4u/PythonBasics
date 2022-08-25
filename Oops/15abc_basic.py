import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        print("Called Abstract Method Area first")
        pass

    def perimeter(self):
        print("Called Abstract Method Perimeter first")
        pass

class Rectangle(Shape):
    def __init__(self, x, y):
        self.l = x
        self.b = y
    # def pprinting(self):
    #     return self.l * self.b
    #TypeError: Can't instantiate abstract class Rectangle with abstract methods area

    def area(self):
        Shape.area(self)
        Shape.perimeter(self)
        return self.l * self.b


r = Rectangle(10,20)

#print('area:' , r.pprinting())
print("Area:", r.area())

# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def area(self):
#         pass
#
# @Shape.register
# class Rectangle():
#     def __init__(self,x,y):
#         self.l = x
#         self.b = y
#
#     def area(self):
#          return self.l * self.b
#
# r = Rectangle(10,20)
# print('area:' , r.area())