class Polygon:
    def __init__(self, no_of_sides):
        print("am in polygon loop")
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        print (self.sides)

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class gon:
    def __init__(self, no_of_sides):
        print("am in gon loop")
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        print (self.sides)

    def inputSides(self):
        print("am in gon loop")
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        print("am in gon loop")
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon, gon):
    def __init__(self):
        print("am ravi")


    def sides(self):
        #Polygon.__init__(self,3)
        super().__init__(3)
    
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

    def restructure(self, parent1, parent2):
        self.__class__.__bases__ = (parent1, parent2, )

    def printBaseClasses(self):
        print (self.__class__.__bases__)
 
t = Triangle()
t.restructure(gon, Polygon)
t.sides()
t.printBaseClasses()
t.inputSides()
t.dispSides()
t.findArea()
