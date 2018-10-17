import pandas as pd
import numpy as np

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

store_items = pd.DataFrame(items2, index = ["store 1", "store 2", "store 3"])
print(store_items)

print(store_items.isnull())

print(store_items.isnull().sum())

# It finds total NaN count
print(store_items.isnull().sum().sum())

# To find total not NaN count

print(store_items.count())

### Eliminate rows or columns contain Nan

# Dropping Rows with NaN values
x = store_items.dropna(axis = 0 )
print(x)

# Dropping Columns with NaN values
y = store_items.dropna(axis = 1)

print(y)

### Replace NaN values now with .fillna()

zero = store_items.fillna(0)

print(zero)

## Forwards filling - fill with previous known value along the choosen axis

fwd = store_items.fillna(method = 'ffill', axis = 0)

print(fwd)

## Backward filling - fill with next known value along choosen axis

bkwd = store_items.fillna(method = "backfill", axis = 1)

print(bkwd)

## Use different interpolation methods

interpolated = store_items.interpolate(method ='linear', axis = 0)
print(interpolated)

## Use different interpolation methods

interpolated = store_items.interpolate(method ='linear', axis = 1)
print(interpolated)

## Quiz Questions

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])


dat = {'Author': authors, 'Book Title': books, 'User 1': user_1,
'User 2': user_2, 'User 3': user_3, 'User 4': user_4}

book_ratings = pd.DataFrame(dat)
print(book_ratings)
book_ratings.fillna(book_ratings.mean(), inplace= True)
print(book_ratings)

