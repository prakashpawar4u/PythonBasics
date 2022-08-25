tup = ('a', "b", "c", "d")
l = "e f g h".split()

print("List type of: {} & its size is: {}".format(type(l), l.__sizeof__()))
print("Tup type of: {} & its size is: {}".format(type(tup), tup.__sizeof__()))

d = {}
d[tup]= "this iw tup "

print(d)
# d[l]= "it will not work"
# print(d)

#LAMBDA
mx = lambda x,y : x if x > y else y
print(mx(8,3))

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print("Squarred :",squared)

# count no of words starting with S:
inp = "this is the input String, In this string words should start with s"
l = inp.split(' ')

count = list(map(lambda x: x[0]=="s" or x[0]=="S", l)).count(True)
print(count)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

n=[4,3,2,1]
print(list(filter(lambda x: x > 2, n)))