import re
import pdb
import inspect
pat = "bxyzca"
st = "xabcabcazzbc"

#Output : str = "bbbcccaaa"
#
# nd = {}
# for i in pat:
#     print(i)
#     occ = re.findall(i, str)
#     #print(occ)
#     nd[i]= occ
# print("DIct:",nd)
#
# print("Keys:", nd.keys())
# print("Values:",nd.values())
MAX_CHAR = 26


def sortByPattern(st,pat):
    print(inspect.stack()[0][3])
    global MAX_CHAR
    count = [0] * MAX_CHAR

    #pdb.set_trace()
    #count number of occurences of each char
    for i in range(0, len(st)):

        count[ord(st[i])-97]+=1
    print(type(count), count)

    #Traverse the pattern and print every characters
    index = 0
    st1 = ''

    for i in range(0,len(pat)):
        j = 0
        while(j < count[ord(pat[i]) - ord('a')]):
            st1 += pat[i]
            j = j+1
            index +=1
    return st1


print(sortByPattern(st, pat))
