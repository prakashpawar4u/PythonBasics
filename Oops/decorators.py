#without disturbing the actual functionality of the existing code
# if you want to perform some action before or after we can decorate that function


def dec_X(func):
    def wrapper_func():
        print("X"*40)
        print("Good Morning")
        func()
        print("X"*40)
    return wrapper_func()

def dec_Y(func):
    def wrapper_func():
        print("Y"*40)
        print("Good Evening")
        func()
        print("Y"*40)
    return wrapper_func()


# @dec_X
# @dec_Y
def say_hello():
    print("Hello World!!!")

hello = dec_Y(say_hello)
#print("HHHH", hello)

#say_hello()