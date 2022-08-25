# #nth Fibonacci Series
# def Fibonacci(n):
#     if n<0:
#         print("Invalid Input:")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# print(Fibonacci(9))

def fib(n):
    a, b = 0,1
    while a < n :
        #print(a, b)
        a, b = b, a+b
        print(a, b)
fib(1)


print("Another")
print("#"*30)

nterms = int(input("How many terms ?"))

n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count +=1