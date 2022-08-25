"""
class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Test: a is %s b is %s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
#print([t]) # This calls __repr__()
print(t) # This calls __str__()

"""

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return("Title:%s, author:%s, pages:%s " %(self.title, self.author, self.pages))

    def __call__(self, price):
        print("Printing Book Details below which costs {} INR".format(price))
        print("Title:%s, author:%s, pages:%s " %(self.title, self.author, self.pages))

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")
book = Book("C in Depth", "Dennis Ritchie", 200)
print(book)
#print([book])
book(500)
print(len(book))
del book
#print(book)
