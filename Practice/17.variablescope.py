# # This function uses global variable s
# def f():
#     print("Inside Function", s)
#
#
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print("Outside Function", s)

# def f():
#     global s
#     s += 'GFG'
#     print("Inside Function", s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s)
#     #s+="Prak"
#
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print("Outside Function :",s)


def f1():
    #global a
    a = 5
    print(a)

a = 10
print('Before:',a)
f1()
print("After:",a)