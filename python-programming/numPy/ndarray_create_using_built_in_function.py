import numpy as np

# ndarray with shape 3x4 with zeros

x = np.zeros((3,4))
print(x)

x = np.zeros((3,4), dtype = int)
print(x)

# ndarray full of ones

x = np.ones((3,4))
print(x)

x = np.ones((3,4),dtype = int)
print(x)

# ndarray full of any numbers

x = np.full((3,4), 5)
print(x)

# Identity matrix ,  An Identity matrix is a square matrix that has only 1s in its main diagonal and zeros everywhere else

x = np.eye(5, dtype=int)
print(x)

# Diagonal Matrix, square matrix that only has values in its main diagonal

x = np.diag([10,20,30,50])
print(x)

# ndarrays that have evenly spaced values within a given interval

x = np.arange(10)
print(x)

x = np.arange(1, 11, 3)
print(x)

# arange when used for non integer result can be mallicious

# In the cases where non-integer steps are required, it is usually better to use the function np.linspace()

x = np.linspace(0,25, 10)
print(x)

x = np.linspace(0,25, 10, endpoint = False)
print(x)

# Using arange and linespace for > 1 rank array

# Use reshape() to comine to create rank 2 ndarrays

x = np.arange(20)
print(x)

x = np.reshape(x, (4,5))

print(x)

# Can call as a method
x = np.arange(20).reshape((4,5))

print(x)

x = np.linspace(0,50,10, endpoint=False).reshape(5,2)
print(x)

# Random ndarray float type

x = np.random.random((3,3))
print(x)

# Random ndarray int type
x = np.random.randint(4,15, size=(3,2))
print(x)

# For example, you may want the random numbers in the ndarray to have an average of 0. 
# NumPy allows you create random ndarrays with numbers drawn from various probability 
# distributions. The function np.random.normal(mean, standard deviation, size=shape),
# for example, creates an ndarray with the given shape that contains random numbers 
# picked from a normal (Gaussian) distribution with the given mean and standard deviation.

x = np.random.normal(0, 0.1, size=(1000, 1000))
print(x)

x = np.arange(2, 34, 2, dtype = int).reshape((4,4))
print(x)