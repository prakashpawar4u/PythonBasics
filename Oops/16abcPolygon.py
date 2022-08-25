from abc import ABC, abstractmethod

# class Polygon(ABC):
#     @abstractmethod
#     def noOfSides(self):
#         pass
#
# class Triangle(Polygon):
#     #overriding abstract method
#     def noOfSides(self):
#         print("I have 3 Sides")
#
#
#
# # Driver code
# R = Triangle()
# R.noOfSides()

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("walk")

class Snake(Animal):
    def move(self):
        print("Crawl")
    
class Dog(Animal):
    def move(self):
        print("Bark")
#driver code
if __name__ == "__main__":
    R = Human()
    R.move()

    K = Snake()
    K.move()