import numpy as np

arr1 = np.array([4,3,2,1])
arr2 = np.array([6,5,4,3])

arr3 = np.setdiff1d(arr1,arr2)

print(arr3)