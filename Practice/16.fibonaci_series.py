def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b , b+a
fib(1000)
