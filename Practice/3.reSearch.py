"""
def swap_list(newlist):
    size= len(newlist)

    temp = newlist[0]
    newlist[0]= newlist[size-1]
    newlist[size-1]=temp

    return newlist

newlist=[1,2,3,4]
print(swap_list(newlist))


newlist=[1,2,3,4]
a = newlist[0]
b = newlist[-1]
#c = b + newlist[1:-1] + a
print(a)
print(b)
print(newlist[1:-1])
newlist[0]=newlist[-1]
newlist[-1]=a
print(newlist)
"""
import re

st= "this is url 10.142.5.8:9090 "
x = re.search("this",st)
print(type(x))

if(x):
    print("Yes we have found a Macth!")
else:
    print("Not found")





    
