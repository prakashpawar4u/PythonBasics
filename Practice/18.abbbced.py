import math
import os
import random
import re
import sys



def create_dict(st,s):
    d={}
    for i in st:
        finDall = re.findall(i,s)
        d[i] = len(finDall)
    return d


if __name__ == "__main__":
    s = 'aanbbdsjfldl;safpoiw9erlfjdsljurfowejdlkfjcosixofwqdklsjfiosjldsfldsjoifnqwelkjfdiohlbbccde'
    st = sorted(set(s))
    d = create_dict(st, s)

    nd = {}
    for k,v in d.items():
        if v not in nd.keys():
            nd[v]=[k]
        else:
            nd[v].append(k)

    print(nd)
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
    print(fd)


    n = 0
    for i ,j in fd.items():
         print(i, j)
         n = n + 1
         if n == 3:
             break