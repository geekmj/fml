import numpy as np

# Dealing with Rank 1 array
x = np.array([1, 2, 3, 4, 5])

print()
print('x = ', x)
print()

# Access element with +ve indices

print('First element in x: ', x[0])
print('2nd element in x: ', x[1])
print('Fifth element in x: ', x[4])

# Access element with -ve indices
print()
print('First element in x: ', x[-5])
print('2nd element in x: ', x[-4])
print('Fifth element in x: ', x[-1])

# Changing Values

x[3] = 20

print()
print('After x[3] = 20, Changed Array, x: ', x)
print()

# Dealing with Rank 2 ndarray now

x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x2
print()
print('x2 = \n', x2)
print()

## Accessing elment

print('This is (0,0) Element in x2:', x2[0][0])
print('This is (0,1) Element in x2:', x2[0][1])
print('This is (2,2) Element in x2:', x2[2][2])

## Modification is also as 1 rank

print()
print('Original:\n x2 = \n', x2)
print()

x2[0,0] = 20

# Modified

print('Modified:\n x2 = \n', x2)

# Adding & Deleting elements

# delete the first and last element of x

x = np.delete(x, [0,4])

print('\nModified x: \n', x)

# delete the first row of x2

w = np.delete(x2, 0, axis = 0)

# delete the first and last column of x2

v = np.delete(x2, [0,2], axis =1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# Appending values to ndarray

# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)

# We print x
print()
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [7,8])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We print v
print()
print('v = \n', v)

# We print q
print()
print('q = \n', q)

## Insert values in ndarrays

# We create a rank 1 ndarray 
x = np.array([1, 2, 5, 6, 7])

# We create a rank 2 ndarray 
Y = np.array([[1,2,3],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x. 
x = np.insert(x,2,[3,4])

# We print x with the inserted elements

print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# NumPy also allows us to stack ndarrays on top of each other,
# or to stack them side by side. 

# We create a rank 1 ndarray 
x = np.array([1,2])

# We create a rank 2 ndarray 
Y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', Y)
# We stack x on top of Y

z = np.vstack((x,Y))

# We stack x on the right of Y. We need to reshape x in 
# order to stack it on the right of Y. 
w = np.hstack((Y,x.reshape(2,1)))

# We print z
print()
print('z = \n', z)

# We print w
print()
print('w = \n', w)