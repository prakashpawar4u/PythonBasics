wordsList = ['this','is','this','is' ,'this','mine']
#For the above given list of words, find the frequency of each word and add it to dictionary
#Output should be in a dictionary as below:
#wordsDict = this -3, is-2, mine-1

wordsDict = {}

for i in wordsList:
    k = wordsDict.keys()
    if i in k:
        wordsDict[i]+=1
    else:
        wordsDict[i]=1

print("wordsDict", wordsDict)

########################
#Another Approach
wordsList = ['this','is','this','is' ,'this','mine']
from collections import Counter
print(Counter(wordsList))
#Out[6]: Counter({'this': 3, 'is': 2, 'mine': 1})


dict11 = {x:wordsList.count(x) for x in wordsList}
print("Dict updated :", dict11)