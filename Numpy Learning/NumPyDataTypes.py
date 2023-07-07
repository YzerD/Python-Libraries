# NumPy Data Types
# Yzer De Gula

import numpy as np

"""
By default, Python has data types:
    strings - used to represent text data
    integer - used to represent integer numbers
    float - used to represent real numbers
    boolean - used to represent True or False
    complex - used to represent complex numbers

Data Types in NumPy:
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type (void)
"""

# Checking the Data Type of an Array
# In NumPy, an array object has a property called dtype that returns
# the data type of the array

arr_1 = np.array([1,2,3,4])
print("Array 1: ", arr_1)
print("Data Type: ", arr_1.dtype)

arr_2 = np.array(['apple', 'banana', 'cherry'])
print("\nArray 2: \n", arr_2)
print("Data Type: ", arr_2.dtype)


# Creating Arrays With a Defined Data Type
# The array() function can take an optional argument: dtype
# This allows us to define the expected data type of the array elements:

arr_3 = np.array([1,2,3,4], dtype='S')
print("\nArray 3: \n", arr_3)
print("Date Type: ", arr_3.dtype)

# For i, u, f, S, and U we can define size as well
arr_4 = np.array([1,2,3,4], dtype='i4')
print("\nArray 4: \n", arr_4)
print("Data Type: ", arr_4.dtype)


# What if a Value Cannot Be Converted?
    # If a type is given in which elements cant be casted then NumPy 
    # will raise a ValueError

    # ValueError: In Python ValueError is raised when the type of passed argument
    # to a function is unexpected/incorrect.
    # arr_5 = np.array(['a', '2', '3'], dtype='i')


# Converting Data Type on Existing Arrays
    # The best way to change the data type of an existing array, is to make a
    # copy of the array with the astype() method.
    #
    # The astype() function creates a copy of the array, and allows you to
    # specify the data type as a parameter.

arr_5 = np.array([1.1, 0, 3.1])
print("\nArray 5: \n", arr_5)
print("Data Type: ", arr_5.dtype)

new_arr_5 = arr_5.astype('i')
print("\nNew Array 5: \n", new_arr_5)
print("Data Type: ", new_arr_5.dtype)

new_arr_5_2 = arr_5.astype(int)
print("\nNew Array 5: \n", new_arr_5_2)
print("Data Type: ", new_arr_5_2.dtype)

new_arr_5_3 = arr_5.astype(bool)
print("\nNew Array 5: \n", new_arr_5_3)
print("Data Type: ", new_arr_5_3.dtype)


