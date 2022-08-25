l1 = [2, 2, 93, 3, 3, 93, 4, 104, 104, 5, 6, 6, 6, 22, 33, 45, 64, 64, 64, 65, 65, 65]
#l1 = [2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 22, 33, 45, 64, 64, 64, 65, 65, 65]

#first iteration
l1.sort()
l2 = []
l2.append(l1[-1])
for i in range(1,len(l1)):
    print(i,l1[-i])
    if l1[-i] != l2[0]:
        l2.append(l1[-i])
        if len(l2)==2:
            break
sumof = (l2[0]+l2[1])
print("Second List :",l2)
print("Addition of 2 values :{}".format(sumof))