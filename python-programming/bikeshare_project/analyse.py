import pandas as pd

df = pd.read_csv("chicago.csv")
print("DataFrame: ", df.head())  # start by viewing the first few rows of the dataset!
print("Columns: ", df.columns)
print("No of missing values: ", df[['Birth Year', 'Gender']].isnull().sum().sum())