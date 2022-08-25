# class Animal():
#     def __init__(self):
#         print("Animal created")
#
#     def whoAmI(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def whoAmI(self):
#         print("Dog")
#
#     def bark(self):
#         print("Woof!")
#
#     def eat(self):
#         print("Eating in Child class")
#
# d = Dog()
# d.whoAmI()
# d.eat()
# d.bark()

class Animal():
    def __init__(self):
        print("Animal created")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def eat(self):
        print("Eating in Child class")


d = Dog()
#d.whoAmI()
d.eat()
#d.bark()


class Parent():
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        #super().show()
        print("Inside Child")

obj = Child()
obj.show()