import inspect
class Foo:
    def __init__(self):
        self.value=42
    def __str__(self):
        return str(self.value)

    def fun2(self):
        print("Calling FUN2")
        print("Calling from {}".format(inspect.stack()[0][3]))

    def fun1(self):
        print("Inside Fun:")
        print(self.value)
        self.fun2()

f=Foo()
#print (f.value)
print(f)
f.fun1()
#print(f)
