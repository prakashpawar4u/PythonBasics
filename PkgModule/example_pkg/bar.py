def bar_func():
    print('this is a bar function')
    print("__name__ :",__name__)

if __name__=="__main__":
    print("Invoked from Main method")
    bar_func()
else:
    print ("Executed when imported")