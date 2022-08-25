"""#ENCAPSULATION:
#
# class Person:
#     __hiddenVar = 10
#     def __init__(self):
#         self.A = "Yuan"
#         self.__B = "private"
#
#
#     def PrintName(self):
#         print(self.A)
#         print(self.__B)
#
# P = Person()
# print(P.A)   # Yuan
# #print(P.__B) # ERROR Accessing private variable failed
#
# P.PrintName()
# #data hiding
# print(P._Person__hiddenVar)



# class MyClass:
#     # Hidden member of MyClass
#     __hiddenVariable = 0
#
#     # A member method that changes
#     # __hiddenVariable
#     def add(self, increment):
#         self.__hiddenVariable += increment
#         print(self.__hiddenVariable)
#
#
# # Driver code
# myObject = MyClass()
# myObject.add(2)
# myObject.add(5)


# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is employee
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

#Rambo = Person("Ram")
#print(Rambo.getName())

#Driver code
emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())


emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())

##############################################

class Base:
    pass #EMpty Class

class Derived(Base):
    pass

print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

print(isinstance(b,Derived))
print(isinstance(b,Base))
print(isinstance(d,Base))
print("Dametukusita",isinstance(d,Base))


# Python example to show working of multiple
# inheritance
print("#*"*30)
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# Base1
# Base2
# Derived
# Geek1 Geek2
#############################################################

print("#*"*30)
class Base:
    # Constructor
    def __init__(self, x):
        self.x = x
class Derived(Base):
    def __init__(self,x,y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(Base.x, self.y)

d = Derived(10,20)
d.printXY()
#####################################
#Using Super class
print("#*"*30)
class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x

class Derived(Base):
    def __init__(self, x, y):
        #super().__init__(name)
        #super().__init__(x)
        super(Derived, self).__init__(x)
        self.y = y

    def printXY(self):
        # Note that Base.x won't work here
        # because super() is used in constructor
        print(self.x, self.y)

d = Derived(10,20)
d.printXY()

##############################
# Class for Computer Science Student
print("#*"*30)
class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"
"""

#class variables using class name only.
# Program to show how to make changes to the
# class variable in Python
# Class for Computer Science Student


class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


# New object for further implementation
a = CSStudent("check", 3)
print("a.stream =", a.stream)

# Correct way to change the value of class variable
CSStudent.stream = "mec"
print("\nClass variable changes to mec")


# New object for further implementation
b = CSStudent("carter", 4)
print ("\nValue of variable steam for each object")
print ("a.stream =", a.stream)
print ("b.stream =", b.stream)
