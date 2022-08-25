l = [1,2,3,4,8]
"""
def my_append(list_1, item_to_add):
   a = len(list_1)
   list_1[a+1]=item_to_add
   return list_1

my_append(l, 5)
"""
mx = lambda x,y: x+y
print(mx(3,5))

my_append = lambda l1, item: print(l1[len(l1)-1], item)
my_append(l, 88)