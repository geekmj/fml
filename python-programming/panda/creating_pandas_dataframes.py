import pandas as pd
import numpy as np

# We create a dictionary of Pandas Series

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']), 
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}
print(type(items))

# We got dictionary create a DataFrame represent 
# shopping carts of Alice and Bob

shopping_carts = pd.DataFrame(items)
print(shopping_carts)

# We create a dictionary of Pandas series without indexes

data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}
# We create a DataFrame
df = pd.DataFrame(data)

print(df)

# Above we can see that Pandas indexes 
# the rows of the DataFrame starting from 0, Just like NumPy 
# indexes ndarrays

# Few information from Pandas DataFrames

print('Shape: ', shopping_carts.shape)
print('Dimensions: ', shopping_carts.ndim)
print('Total elements: ', shopping_carts.size)
print('Values in shopping cart: ', shopping_carts.values)
print('Row index: ', shopping_carts.index)
print('Column index: ', shopping_carts.columns)

# Choosing what data used of pased Dictionary when creating 
# DataFrames

## Choose to pick specific column index
bob_shopping_cart = pd.DataFrame(items, columns = ['Bob'])

print(bob_shopping_cart)

## Choosing which specific rows data to use

# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

print(sel_shopping_cart)

## Create DataFrame with selected row item and column index

# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, columns = ['Alice'], index = ['glasses', 'bike'])
print(alice_sel_shopping_cart)

## Manually create DataFrames from dictionary of lists (arrays)
# Make sure all the lists (arrays) are of same length

# We create a dictionary of lists (arrays)
data = {
    'Integers' : [1,2,3],
    'Floats' : [4.5, 8.2, 9.6]
}

df = pd.DataFrame(data)

print(df)

# Notice data dictionary we created don't have label indices, So
# it used Numericals row index

# While creating DataFrame from list, we can provide row index

df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])
print(df)

## Creating DataFrame using list of Python Dictionaries

items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
           {'watched': 10, 'glasses': 50, 'bikes':15,'pants': 5 } 
        ]
store_items = pd.DataFrame(items2)
print(store_items)
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])
print(store_items)




