# wordsList = ['this','is',this','is,this','mine']
# wordsDict = this -3, is-2, mine-1
#
# input = "abcdefgh"
# output - "cba fed gh"
#
# "Hi There How are you doing"
# (H)i (T)here (H)ow are you doing
#
# http://10.10.200.1:99/index.html



##################################################
wordsList = ['this','is',"this",'this','mine']
# wordsDict = this -3, is-2, mine-1
d = {}

for i in wordsList:
    if i in d.keys():
        d[i]=(int(d[i]) + 1)
    else:
        d[i]=1

print("DIct",d)

##################################################
inp = "abcdefgh"
n = 3
str3=[]

for i in range(0,len(inp),n):
    str2 = inp[i:i+n]
    if len(str2)==3:
        str3.append(str2[::-1])
    else:
        str3.append(inp[i:i+n])

# output - "cba fed gh"
print(str3)
print(" ".join(str3))


##################################################
"Hi There How are you doing"
# (H)i (T)here (H)ow are you doing
l2 = []
st = "Hi There How are you doing"

l = st.split(" ")
print(l)
for i in l:
    if i[0].isupper():
        l2.append("({}){}".format(i[0],i[1:]))
    else:
        l2.append(i)
print("L2:",l2)


##################################################
url = "http://10.10.200.1:99/index.html"

import re



##################################################
#sort 2nd strings on the order of first
#Input  : pat = "bxyzca", str = "abcabcabc"
#Output : str = "bbbcccaaa"

pat = "bxyzca"
st = "abcabcabc"
newst = []
di = ""
for i in pat:
    print(i)
    for j in st:
        if j==i:
            #newst.append(j)
            di += j
        else:
            print("not found")
#print("New ST", newst)
print("New ST", di)

################################
import pdb

MAX_CHAR = 26
# Sort str according to the order defined by pattern.
def sortByPattern(str, pat):
    global MAX_CHAR
    pdb.set_trace()
    count = [0] * MAX_CHAR
    for i in range(0, len(str)):
        count[ord(str[i]) - 97] += 1
        index = 0;

        str = ""

        for i in range(0, len(pat)):
            j = 0
            while (j < count[ord(pat[i]) - ord('a')]):
                str += pat[i]
                j = j + 1
                index += 1

        return str

# Driver code
pat = "bca"
str = "abc"
print(sortByPattern(str, pat))
