

def countSetbits(num):
    bina = bin(num)
    print(num, ":", bina)

if __name__ == "__main__":
    num = 10
    for i in range(15):
        countSetbits(i)
