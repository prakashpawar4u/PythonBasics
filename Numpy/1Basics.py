import numpy as np
mylist = [1,2,3,4,5]
print(mylist)
np.array(mylist)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

print("Array", np.array(my_matrix))
print("Arange", np.arange(0,10))

print(np.arange(0,11,2))

print(np.zeros(3))
print(np.zeros((5,5)))

print("Ones", np.ones((3,3)))

print("Linspace", np.linspace(5,10,20))

print("Eye", np.eye(5))

print("Randn Single", np.random.randn(2))
print("Random Array", np.random.randn(5,5))

print("Random Int:", np.random.randint(5))
print("Random Int List: ", np.random.randint(5, 15, 5))#from, to, how many

print("arange 25:",np.arange(25))
print("ranarr:", np.random.randint(0,50,10))

arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

print("Reshape: ", arr.reshape(5,5))
print("Ranarr Max: ", ranarr.max())
print("Ranarr argmax(): ",ranarr.argmax())
print("ranarr.min(): ", ranarr.min())
print("ranarr.argmin: ",ranarr.argmin())

#Shape
print("Shape:", arr.shape)
print("Reshape:", arr.reshape(1,25)).shape ()
print(arr.reshape(1,25))
print("Hello:", arr.reshape(25,1))
print(arr.dtype)
