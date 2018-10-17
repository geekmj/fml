import numpy as np

x = np.array([1, 2, 3, 4, 5])

print(x)
print(type(x))
print(x.dtype)
print(x.shape)

# Two dimensional array

x2 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
print(x2)
print(x2.size)
print(x2.shape)

# 3D

x3 = np.array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])

print(x3)
print(x3.size)
print(x3.shape)