if __name__ == '__main__':
    a = int(input())
    b = int(input())

    s1 = lambda a,b: a+b

    sub = lambda a,b: a-b

    pro = lambda a,b: a*b

    print(s1(a,b))
    print(sub(a,b))
    print(pro(a,b))