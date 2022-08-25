#from collections import Counter
import collections
wordsList = ['this','is','this','is,this','mine']

#ctr = collections.Counter(wordsList)
#print(ctr)
def freq(word):
    dic = {}
    for i in word:
        if i in dic.keys():
            dic[i] +=1
        else:
            dic[i] = 1
    print("Frequency:", dic)
    return dic

duplicate = [0,0,0,1,1,2,2,3,3,4,5,6,7,8]
char_freq = freq(duplicate)
print()
uniq = []
for i in char_freq:
    if char_freq[i]==1:
        uniq.append(i)

print(uniq)
