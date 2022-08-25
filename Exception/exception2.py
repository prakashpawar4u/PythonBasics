print("Exception handelling:\n")
try:
    print("In try block")
    l = [1,2,3]
    #print(l[10]+1/0)
    print(l[1])
    a = 1/0
except ZeroDivisionError:
    print("Zero division error occured")
except:
    print("some other error")
else:
    print("in else block")
    print("No runtime error")
finally:
    print("This will always be called")
