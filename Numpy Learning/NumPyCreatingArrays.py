# NumPy Creating Arrays
# Yzer De Gula 

import numpy as np

print("Version: ", np.__version__)

# We can create a NumPy ndarray object using the array() function
# type() function tells us the type of the object passed into it.
# type is numpy.ndarray 
arr = np.array([1,2,3,4])
print("Test Array: \n", arr, type(arr), "\n")


# Dimensions in Arrays

# 0-D Arrays, or Scalars, are the elements in an array
# Each value in an array is a 0-D array.
array_zeroD = np.array(24)
print("Zero-Dimensional Array: ") 
print("Dimensions: ", array_zeroD.ndim)
print("Array: \n", array_zeroD, "\n")


# 1-D Arrays, are arrays that has 0-D arrays as its elements (Vector?)
array_oneD = np.array([1,2,3,4,5])
print("One-Dimensional Array: ") 
print("Dimensions: ", array_oneD.ndim)
print("Array: \n", array_oneD, "\n")

# 2-D Arrays, an array that has 1-D arrays as its elements (Matrix?)
array_twoD = np.array([[1,2,3], [4,5,6]])
print("Two-Dimensional Array: ") 
print("Dimensions: ", array_twoD.ndim)
print("Array: \n", array_twoD, "\n")

# 3-D Arrays, an array that has 2-D arrays (matrices) as its elements
array_threeD = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print("Three-Dimensional Array: ") 
print("Dimensions: ", array_threeD.ndim)
print("Array: \n", array_threeD, "\n")

# We can use the ndim attribute that reutns an integer that 
# represents how many dimensions the array has.

# Higher Dimensional Arrays:
# An array can have any number of dimensions
# We can define these by using the ndmin argumment
# arr = np.array([1,2,3,4], ndmin = 5)