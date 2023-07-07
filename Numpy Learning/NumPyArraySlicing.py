# NumPy Array Slicing
# Yzer De Gula 

import numpy as np

# Slicing Arrays
# Slicing in Python means taking elements from one given index to another
# We slice like this: [start:end]
# We can also slice like this: [start:end:step
# 
# If we don't pass Start, it's considered 0
# If we don't pass End, it's considered the length of the array
# If we don't pass Step, it's considered 1

arr_1 = np.array([1,2,3,4,5,6,7])
print("Array 1: \n", arr_1)
# NOTE: The result INCLUDES the start index, but EXCLUDES the end index
print("Elements from 1 to 5: ", arr_1[1:5])
print("Elements from 4 to End: ", arr_1[4:])
print("Elements from the beginning to 4: ", arr_1[:4])

# Negative Slicing
# Use the minus operator to refer to an index from the end:
print("Elements from 3 from the end to 1: ", arr_1[-3:-1])


# STEP
# Use the step value to determine the step of the slicing:
print("Every Other Element from 1 to 5: ", arr_1[1:5:2])
print("Every Other Element from the Entire Array: ", arr_1[::2])


# Slicing 2-D Arrays
arr_2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("\nArray 2: \n", arr_2)
# NOTE: Remember that second element has index 1, and that end is exclusive
print("From the Second Element, Slice Elements From 1 to 4: ", arr_2[1, 1:4])
print("From Both Elements, Return Second Element: ", arr_2[0:, 2])
print("From Both Elements, Slice 1 to 4: \n", arr_2[0:, 1:4])