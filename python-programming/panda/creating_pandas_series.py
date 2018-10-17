import pandas as pd

# A Pandas series is a one-dimensional array-like object that can hold many data types, such as numbers or strings
# One of the main differences between Pandas Series and NumPy ndarrays
#  is that you can assign an index label to each element in the
#  Pandas Series. In other words, you can name the indices of your
#  Pandas Series anything you want. Another big difference between
#  Pandas Series and NumPy ndarrays is that Pandas Series can hold
#  data of different data types.

# Creating a Panda Series that stores a grocerry list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
print(groceries)

# We see that Pandas Series are displayed with the indices in the
# first column and the data in the second column. Notice that
# the data is not indexed 0 to 3 but rather it is indexed with
# the names of the food we put in, namely eggs, apples, etc... 
# Also notice that the data in our Pandas Series has both integers
# and strings.

print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of ', groceries.size, 'elements')

# We print the index and data of Groceries
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)

# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)