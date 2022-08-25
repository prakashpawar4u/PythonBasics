import math
import os
import random
import re
import sys

def create_dict(st):
    d = {}
    for i in st:
        if str(s.count(i)) not in d:
            d[str(s.count(i))] = []
            d[str(s.count(i))].append(i)
        else:
            d[str(s.count(i))].append(i)
    return d


#s = 'aanbbbbccde'
s = "aabbbccde"
st = set(s)
d = create_dict(st)
print ("first dict:",d)
print("#~"*30)


nd = {}
for k in d.keys():
    nd[k]=sorted(d[k])
print("sorted:",nd)

l1 = sorted(nd.keys())
l2 = l1[::-1]
print("#"*30)
final_d = {}
for i in l2:
    if len(nd[i]) > 1:
        for j in range(0,len(nd[i])):
            final_d[nd[i][j]]= i
    else:
        #print("length is 1:")
        final_d[nd[i][0]]=i

print(final_d)
# n = 0
# for i ,j in final_d.items():
#      print(i, j)
#      n = n + 1
#      if n == 3:
#          break