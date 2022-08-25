# Python example to check if a class is
# subclass of another

class Base():
    print("calling base class from the derived")
    pass#empty

class Derived(Base):
    pass

print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

print(isinstance(b, Derived))
print(isinstance(d, Base))