# class CSSStudent:
#     stream = "cse"
#
#     #class variable or static variable
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#
# a = CSSStudent("Amal", 1)
# b = CSSStudent("Ashwin", 3)
#
# #Amal
# print("~"*30)
# print(a.stream)
# print(a.name)
# print(a.roll)
#
# #Ashwin
# print("~"*30)
# print(b.stream)
# print(b.name)
# print(b.roll)
#
# #class variables can be accessed by Classname also
# print("~"*30)
# print(CSSStudent.stream)
# #print(CSSStudent.name)

# class Fruits:
#     count = 0
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#         Fruits.count = Fruits.count + count
#         #print("Fruit Count :", Fruits.count)
#
# if __name__ == "__main__":
#     print("Inside Main")
#     ob = Fruits("Apple", 3)
#     ob2 = Fruits("Banana", 6)
#     ob3 = Fruits("Berries", 10)
#     print("Final Count of Fruits are:",Fruits.count)

# from datetime import date
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     #A class method to create a Person object by Birth year
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
# person1 = Person("Prakash", 31)
# print(person1.name)
# print(person1.age)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

print("#"*30)
print(hasattr(emp1, 'name'))  # Returns true if 'age' attribute exists
print(getattr(emp1, 'name'))    # Returns value of 'age' attribute
print(setattr(emp1, 'name', "PAKKU"))  # Set attribute 'age' at 8
print(emp1.name)
#delattr(empl, 'age')
print("#"*30)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)