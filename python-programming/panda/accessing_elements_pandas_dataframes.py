import pandas as pd

items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
           {'watches': 10, 'glasses': 50, 'bikes':15,'pants': 5 } 
        ]
store_items = pd.DataFrame(items2, index = ['Store 1', 'Store 2'])

print(store_items)

## We can access rows, columns, or individual elements of the DataFrame
# by using the row and column labels.

print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes','pants']])

## Check [[]], while [] worked for one index but not for 2

print()
print('How items are in in Store 1:\n', store_items.loc[['Store 1']])
print()

## Notice for accessing row u have to use loc

print('How many bikes are in Store 2:\n', store_items['bikes']['Store 2'])
## Notice Column first than row

## For modification we can use dataframe[column][row]

## Adding a column named shirts, provide info shirts in stock at each store
store_items['shirts'] = [15,2]
print(store_items)

## It is possible to add a column having values which are outcome
# of arithmatic operation between other column

# New Suits column with values addition of number of shirts and pants

store_items['suits'] = store_items['shirts'] + store_items['pants']
print(store_items) 

## To add rows to our DataFrame we first have to create a new Dataframe
# and than append

# New dictionary
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# New dataframe
new_store = pd.DataFrame(new_items, index = ['Store 3'])

print(new_store)

# Use append and add it to existing dataframe
store_items = store_items.append(new_store)
print(store_items)

# Notice Alphabetical order in which they appended

# we add a new column using data from particular rows in the watches column

store_items['new watches'] = store_items['watches'][1:]
print(store_items)

# Insert a new column with label shoes right before the 
# column with numerical index 4

store_items.insert(4, 'shoes', [8,5,0])

print(store_items)

## .pop() delete column and .drop() to delete row

store_items1 = store_items.pop('new watches')
print(store_items1)

# Remove the store 2 and store 1 rows

store_items2 = store_items.drop(['Store 2', 'Store 1'], axis = 0)
print(store_items2)

# Change row and column label

store_items = store_items.rename(columns = {'bikes': 'hats'})

print(store_items)

store_items = store_items.rename(index = {'Store 3': 'Last Store'})

print(store_items)

# We change the row index to be the data in the pants column
store_items = store_items.set_index('pants')

# we display the modified DataFrame
print(store_items)