# NumPy Array Indexing
# Yzer De Gula 

import numpy as np

# Access Array Elements
# Array indexing is the same as accessing an array element
# Access an array element by referring to its index number
# Array is 0-indexed

arr_1 = np.array([1,2,3,4])
print("Array 1: \n", arr_1)
print("First Element: ", arr_1[0])
print("Second Element: ", arr_1[1])
print("Sum of Third & Fourth Element: ", arr_1[2] + arr_1[3])


# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma seperated integers
# representing the dimension and the index of the element.

# Think of 2-D Arrays as a table with rows and columns, where the dimension
# represents the row and the index represents the column.

arr_2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("\nArray 2: \n", arr_2)
print("Element in First Row, Second Column: ", arr_2[0, 1])
print("Element in Second Row, Fifth Column: ", arr_2[1, 4])


# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma seperated integers
# representing the dimensions and the index of the element.

arr_3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("\nArray 3: \n", arr_3)
print("Third Element of the Second Array of the First Array: ", arr_3[0, 1, 2])

"""
arr_3[0, 1, 2] prints the value 6

The FIRST number represents the first dimension, which contains two arrays:
[[1,2,3], [4,5,6]]
and:
[[7,8,9], [10,11,12]]

Since we selected 0, we are left with the first array:
[[1,2,3,], [4,5,6]]


The SECOND number represents the second dimension, which also contains two arrays:
[1,2,3]
and:
[4,5,6]

Since we selected 1, we are left with the second array:
[4,5,6]


The THIRD number represents the third dimension, which contains three values:
4
5
6

Since we selected 2, we end up with the third value:
6
"""

# Negative Indexing
# Use negative indexing to access an array from the end/

arr_4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("\nArray 4: \n", arr_4)
print("Last Element From Second Dimension: ", arr_4[1, -1])