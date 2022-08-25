import abc
from abc import ABC, abstractmethod

class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "Parent Class"

class child(parent):
    @property
    def geeks(self):
        #print(parent.geeks)
        return "child class"


try:
    r = parent()
    #r = child()
    print(r.geeks)
    #Can't instantiate abstract class parent with abstract methods geeks
except Exception as err:
    print(err)

r = child()
print(r.geeks)


#https://www.geeksforgeeks.org/abstract-classes-in-python/
