import numpy as np
import pandas as pd

arr = np.arange(0,21)
print(arr)

arr2 = np.array([1,2,3,4,5])
print(arr2)


labels = "a b c d e".split(" ")
mylist = [1, 2, 3, 4, 5]
arr = np.array([10, 20, 30, 40, 50])
d = {}
for i in labels:
    #print(i)
    #print("Index:", labels.index(i))
    d[i]=arr[labels.index(i)]

print("Dict :", d)

print(pd.Series(data = mylist))
print(pd.Series(data=mylist, index= labels))

print(pd.Series(d))
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
print(ser2["Italy"])
print(ser1 + ser2)


##########################
#DATA FRAMES
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4), index="A B C D E".split(), columns="W X Y Z".split())
print(df["W"])
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df)

df.drop('new', axis= 1, inplace=True)
print(df)
#loc represents row "A"
print(df.loc['A'])
#iloc represents row based on index
print(df.iloc[2])

print(df.loc['B','Y'])
print(df.loc[["A", "B"], ["W","Y"]])


