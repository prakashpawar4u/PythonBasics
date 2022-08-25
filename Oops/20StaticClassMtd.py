from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Class method to create a Person object by birth
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year -year)

    #Static method to check if a Person is adult or not

    @staticmethod
    def isAdult(age):
        return age > 18

p1 = Person('Prakash',21)
p2 = Person.fromBirthYear('Mayank',1995)

print(p1.name, p1.age, p1.isAdult(p1.age))
print(p2.name, p2.age, p2.isAdult(p2.age))



#print()