def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)


if __name__ == "__main__" :
    n = 320
    factors(n)