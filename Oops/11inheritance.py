class Parent:        # define parent class
   parentAttr = 100
   __hiddenVar = "MyHidd"
   def __init__(self):
      print("Calling parent constructor")

   def _parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()
p = Parent()
# instance of child
c.childMethod()      # child calls its method
c._parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
print(c._Parent__hiddenVar)

###isinstance & isvar
print(issubclass(Child,Parent))
print(issubclass(Parent,Child))

print(isinstance(c, Parent))
print(isinstance(p, Child))
