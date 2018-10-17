import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

print(df.head())

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

print(df['hour'].head())
# find the most common hour (from 0 to 23)
popular_hours = df.groupby(['hour'], sort=False)['hour'].count()

print(popular_hours)

popular_hour = popular_hours.idxmax()

print('Most Frequent Start Hour:', popular_hour)