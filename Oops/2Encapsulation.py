class Test:
    i = 123
    def __init__(self):
        print("Init method called")
    def func(self):
        return "func called "

x = Test()
print(x.i)
print(x.func())


print("#"*30)
#Encapsulation
class Person:
    def __init__(self):
        self.A = "Yuan"
        self.__B = "private"

    def PrintName(self):
        print(self.A)
        print(self.__B)

p = Person()
p.PrintName()
print(p.A)
#print(p.__B) # will throw Error
print(p._Person__B) #object._Class__PrivateVar