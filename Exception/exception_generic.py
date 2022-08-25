print("Exception handelling:\n")
try:
    a= 10
    print("In try block")
    print(a)
except Exception as e:
    print("In Exception block")
    print(e)
# except ZeroDivisionError:
#     print("Zero division error occured")
# except:
#     print("some other error")
# else:
#     print("in else block")
#     print("No runtime error")
# finally:
#     print("This will always be called")
