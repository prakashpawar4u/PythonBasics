import math
import os
import random
import re
import sys
import pdb

"""
#s = 'aanbbbbccde'
s = 'abaaabbzzzzzcddfkcde'
#s = 'MavenirTrustTheFuture'
st = sorted(set(s))
#pdb.set_trace()
d={}
for i in st:
    finDall = re.findall(i,s)
    #print(finDall)
    d[i] = len(finDall)
print("First Dict",d)

nd = {}
for k,v in d.items():
    if v not in nd.keys():
        nd[v]=[k]
    else:
        nd[v].append(k)

print("New Dict:",nd)
l1 = nd.keys()
l2 = nd.values()
print(l1)
print(l2)

fd = {}
for i in (reversed(sorted(nd.keys()))):
    if len(nd[i]) > 1:
        l2 = (sorted(nd[i]))
        for j in range(len(l2)):
            #print(nd[i][j], i)
            fd[nd[i][j]]=i
    else:
        print(nd[i][0], i)
        fd[nd[i][0]] =i

print("###"*40)
print("Final Dict:",fd)


n = 0
for i ,j in fd.items():
     print(i, j)
     n = n + 1
     if n == 3:
         break

"""

my_string = "abaaabbzzzzzcddfkcde"

def testCounter(arg):
    tmp = {}

    for each in arg:
        if each in tmp:
            tmp[each]+=1
        else:
            tmp[each]=1

    rev_tmp = {}
    for key in tmp:
        pdb.set_trace()
        if tmp[key] in rev_tmp:
            rev_tmp[tmp[key]].append(key)
        else:
            rev_tmp[tmp[key]] = [key]

    req = rev_tmp.keys()
    req = sorted(req)[::-1]
    for each in req[:3]:
        for key in rev_tmp[each]:
            print ("{}- {}".format(key, each))

testCounter(my_string)
