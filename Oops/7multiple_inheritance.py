# class Base1(object):
#     def __init__(self):
#         self.str1 = "geek1"
#         print("Base1")
#
#
# class Base2(object):
#     def __init__(self):
#         self.str2 = "Geek2"
#         print("Base2")
#
#
# class Derived(Base1, Base2):
#     def __init__(self):
#         # Calling constructors of Base1
#         # and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#
#     def printStrs(self):
#         print(self.str1, self.str2)
#
#
# ob = Derived()
# ob.printStrs()

############################################################

class Base(object):
    #pass
    # Constructor
    def __init__(self, x):
        self.x = x
        print("\nInside Base:", x)


class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        print("Called Dervied class")
        Base.x = x
        print("assigned value of x")
        self.y = y

    def printXY(self):
        # print(self.x, self.y) will also work
        print(Base.x, self.y)

# Driver Code
d = Derived(10, 20)
d.printXY()
