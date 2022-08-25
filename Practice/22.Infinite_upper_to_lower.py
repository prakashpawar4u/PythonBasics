st = input("Please enter input string:")
out = ''
print("The input is ::", st)

for i in st:
    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        out = out + i
    else:
        k = ord(i)
        l = k + 32
        out = out + chr(l)

print("----------> ", out)
###############################################