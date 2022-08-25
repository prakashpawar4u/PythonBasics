print("Exception handelling:\n")
try:
    print("In try block")
    #print(a[1])
    a = 1/3
except ZeroDivisionError:
    print("Zero division error occured")
except:
    print("some other error")
else:
    print("in else block")
finally:
    print("This will always be called")
