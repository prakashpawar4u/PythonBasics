mx = lambda x,y: x if x > y else y
print(mx(8,4))

#MAP
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


# count no of words starting with S:
inp = "this is the input String, In this string words should start with s"
l = inp.split(' ')
count = list(map(lambda x: x[0]=="s" or x[0]=="S", l)).count(True)
print(count)

#FILTER:
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

n=[4,3,2,1]
print(list(filter(lambda x: x > 2, n)))

#Reduce
from functools import reduce
n = [4,3,2,1]
print(reduce(lambda x,y: x*y, n))

#Zip
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

for i, j in color_dictionary.items():
    print(i,":",j)

#transpose:
l = [[1,2,3,4],[5,6,7,8]]
print(list(map(list,zip(*l))))
print(map(list,zip(*l)))

#JOIN:
a=["a","b","c","d"]
str1="".join(a)
print(str1)
##################################################
#SPLIT:
str1="this is my, fight song"
print(str1.split(","))

#STRIP:
str = "0000000this is string example....wow!!!0000000"
print(str.lstrip('0'))
#this is string example....wow!!!0000000
print(str.rstrip('0'))
#0000000this is string example....wow!!!
print(str.strip('0'))
#this is string example....wow!!!

#removes the char from the begining of the string.
list1 = [1,2,3,4]
list2 = [3,4]
s=set(list2)
temp=[x for x in list1 if x not in s]
print (temp)


#list comprehensions:
l1 = [1,2,4,3,5]
l2 = [3,4]
s= set(l2)
temp = [x for x in l1 if x not in s]
print(temp)

#Dict comprehension
#sq = {x : x*x for x in range(1,6)}
sq = {x : x*x for x in l1}
print("Dict comprehension:", sq)
print(sq.get(3))
d = sq
print("D",d)
d2=sq.copy()
print("D2",d2)


#multiply dict
# for k, v in sq.items():
#     res = res *sq[k]
# print("Multiplication:", res)

def test_var_args(f_arg, *argv):
    print("First Normal arg: ", f_arg)
    for arg in argv:
        print("another agr through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')
test_var_args('python', ['eggs', 'test'])

print("###"*40)
def greet_me(**kwargs):
    for k , v in kwargs.items():
        print("{0} = {1}".format(k,v))
greet_me(name="yasoob")

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}
def f(*args,**kwargs): print(args, kwargs)

f()
f(1,2,3)
f(1,2,3,"groovy")
f(a=1,b=2,c=3)
f(a=1,b=2,c=3,zzz="hi")
f(1,2,3,a=1,b=2,c=3)
f(*l,**d)
f(*t,**d)
f(1,2,*t)
f(q="winning",**d)
f(1,2,*t,q="winning",**d)


