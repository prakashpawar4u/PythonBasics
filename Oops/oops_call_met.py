class Myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Constructor Called\n")

    def __call__(self):
        print("Call Method is invoked automatically:")
        print("I want to Multipy:",self.a * self.b)

    def summattion(self):
        return self.a + self.b

obj = Myclass(4,5)
print("Summation output ::", obj.summattion())
#This will call my call method
#obj()
