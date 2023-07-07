# NumPy Array Copy Vs View
# Yzer De Gula

import numpy as np

"""
The Difference Between Copy and View:
    The main difference between a copy and view of an array is that the copy
is a new array, and the view is just a view of the original array.

The copy OWNS the data and changes made to the copy will not affect original
array, and any changes made to the original array will not affect the copy.

The view DOESN'T OWN the data and any changes made to the view will affect
the original array, and any changes made to the original array will affect
the view.
"""

# COPY:
arr_1 = np.array([1,2,3,4,5])
arr_1_copy = arr_1.copy()
arr_1[0] = 24
print("Array 1: \n", arr_1)
print("Array 1 Copy: \n", arr_1_copy, "\n")

# VIEW:
arr_2 = np.array([6,7,8,9,10])
arr_2_view = arr_2.view()
arr_2[0] = 24
arr_2_view[0] = 65
print("Array 2: \n", arr_2)
print("Array 2 View: \n", arr_2_view, "\n")

"""
Check if Array Owns its Data:
    Copies OWN the data, views DO NOT. NumPy arrays has the attribute base
that returns None if the array owns the data. Otherwise, the base attribute
refers to the original object.
"""

arr_3 = np.array([1,2,3,4,5])
arr_3_copy = arr_3.copy()
arr_3_view = arr_3.view()

print("Array 3: \n", arr_3)
print("Array 3 Copy Base: \n", arr_3_copy.base)
print("Array 3 View Base: \n", arr_3_view.base)
