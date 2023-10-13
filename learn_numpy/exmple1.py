# NumPy gives you an enormous range of fast and efficient ways of creating arrays and manipulating numerical data inside them.
# While a Python list can contain different data types within a single list, all of the elements in a NumPy array should be homogeneous.
# The mathematical operations that are meant to be performed on arrays would be extremely inefficient if the arrays weren’t homogeneous.

# NumPy arrays are faster and more compact than Python lists. An array consumes less memory and is convenient to use.
# NumPy uses much less memory to store data and it provides a mechanism of specifying the data types.
# This allows the code to be optimized even further.

import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

print(a[0])


print(np.zeros(2))

print(np.ones(2))

print(np.arange(2, 9, 2))