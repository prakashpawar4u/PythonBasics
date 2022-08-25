from multiprocessing import Process

def func1():
    print("Func1 is starting")
    for i in range(0,100):
        print("P1:",i)
    print("Func1: Finishing")


def func2():
    print("Func2 is starting")
    for i in range(0,1000):
        print("P22222:", i)
    print("Func2: Finishing")


if __name__ == "__main__":
    p1 = Process(target= func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()