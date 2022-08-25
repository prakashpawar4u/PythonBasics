# Python program to
# demonstrate private methods

# Creating a Base class
class Base:

    # Declaring public method
    def fun(self):
        print("Public method")

        # Declaring private method

    def __fun(self):
        print("Private method")

    # Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)

    def call_public(self):
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()

    def call_private(self):
        # Calling private method of base class
        self.__fun()

# Driver code

obj1 = Base()
obj1.fun()
#obj1.__fun()

obj2 = Derived()
obj2.call_public()
#obj2.call_private()



# Creating a class
class A:

    # Declaring public method
    def fun(self):
        print("Public method")

        # Declaring private method

    def __fun(self):
        print("Private method")

        # Calling private method via

    # another method
    def Help(self):
        self.fun()
        self.__fun()

    # Driver's code


obj = A()
obj.Help()

print("#~"*30)
class A:

    # Declaring public method
    def fun(self):
        print("Public method")

        # Declaring private method

    def __fun(self):
        print("Private method")

    # Driver's code


obj = A()

# Calling the private member
# through name mangling
obj._A__fun()