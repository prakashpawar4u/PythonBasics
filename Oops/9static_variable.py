class Shell:
    #class variable
    classVar = "clsVar"
    _privateVar = "privateVar"
    __protectedVar = "protectedVar"

    def __init__(self):
        print("Constructor Method called:")
        self.a = 10
        self.b = 20
s = Shell()
print(s.classVar)
print(s._privateVar)
#print(s.__protectedVar) # will throw error
print(s._Shell__protectedVar)


