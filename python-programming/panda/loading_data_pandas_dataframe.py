import pandas as pd

# Python have inbult function to read a CSV
# There are many other inbuilt function like
# read_excel(), read_json(), read_clipboard() etc.
# After reading it creates DataFrame

goog_stock = pd.read_csv('./goog.csv')
print(goog_stock)

# We can see not all the rows are print. Only few start and
# Few end

# Check Type
print(type(goog_stock))
# Check shape -> Rows and Columns
print(goog_stock.shape)
# Check size Total Data Points 
print(goog_stock.size)

print("Check if any column have null values \n", goog_stock.isnull().any())

print("5 Records (default) From Beginning\n", goog_stock.head())

print("15 records from beginning\n", goog_stock.head(15))

print("5 records (default) from end\n", goog_stock.tail())

print("15 records (default) from end\n", goog_stock.tail(15))

print("Descriptive statistics on each column \n", goog_stock.describe())

# We can get above data individually too
print("Max Value of each column\n", goog_stock.max())

print("Average (mean) Value of each column\n", goog_stock.mean())

## Correlation is a statistical measure that indicates the extend to which
# two or more variable fluctuate together. A positive correlation indicates
# extend to which those variable increases or decreases in parallel.
# A negative correlation indicates the extend to which one variable increases 
# as the other decreases.

print("Data Correlation for different columns\n", goog_stock.corr()) 

## Advance reporting with groupby() method
# Well it groups a column and than we can work on those data
# set

fake_company = pd.read_csv('./fake_company.csv')
print(fake_company)

# Find year & salary expense
# Group on Year  and sum on salary
print("Yearwise salary expese\n", fake_company.groupby(['Year'])['Salary'].sum())

print("Average Salary of each year\n", fake_company.groupby(['Year'])['Salary'].mean())

print("Employee wise salary in years\n", fake_company.groupby(['Name'])['Salary'].sum())

print("Salary distribution per year per department \n", fake_company.groupby(['Year','Department'])['Salary'].sum())