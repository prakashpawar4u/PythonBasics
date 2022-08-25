import inspect
import os
def test1():

    print("File Name:",os.path.dirname(__file__), __file__)
    print("Function name:", inspect.stack()[0][3])
    print("Called from a file 1")


def test2():
    print("Called from a file 1")
    print("Function name:", inspect.stack()[0][3])
    print("file:",os.path.abspath(os.path.dirname(__file__)))

