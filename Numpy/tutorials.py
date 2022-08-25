import numpy as np

#creating a rank 1 array
arr = np.array([1,2,3,4])
print("Array with Rank 1:\n",arr)

#create a rank 2 array
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print("Array 2:",arr2)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)


l = [1,2,3,4]
arr = np.array(l)
print("Array with Rank 11:\n",arr)
