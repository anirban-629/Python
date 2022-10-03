import numpy as np
import sys
arr1=[1,2,3,4,5]
arr2=np.array([1,2,3,4,5],np.int8)
print("Same Array: ",arr1)
print("Size of Python array",sys.getsizeof(1) * len(arr1))
print("Size of Numpy array",arr2.itemsize * arr2.size)
print(arr2)
#dtype int8 means data type integer of 8bit=1byte
