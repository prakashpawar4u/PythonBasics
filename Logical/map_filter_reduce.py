l = [1,2,4,5,6,7,78]
sq  = list(map(lambda x: x**2, l))
print("Square: ", sq)

inp = "this is the input String, In this string words should start with s"
l = inp.split(' ')
count = list(map(lambda x: x[0]=="s" or x[0]=="S",l)).count(True)
#count = list(map(lambda x: x[0]=="s" or x[0]=="S", l)).count(True)
print("COunt",count)

####################
print("##"*40)
num_list = list(range(-5,5))
print(num_list)
fil = list(filter(lambda x : x<0 , num_list))
print("FILTER", fil)


num_list2 = range(1,10)
fil2 = list(filter(lambda x : x > 8, num_list2))
print("FILTER2 ", fil2)
print("##"*40)

from functools import reduce
product = reduce((lambda x, y: x*y), range(1,5))
print("Product : ", product)

prod = reduce((lambda x,y: x*y),[1,4,5,6,7,9])
print(prod)

print("##"*40)
l = [[1,2,3,4],[5,6,7,8]]
k = list(map(list,zip(*l)))
print(k)


m = [[1,2],[3,4],[5,6]]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)
