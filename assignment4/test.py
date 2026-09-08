import pandas as pd

## Sample DataFrame with mixed data types
#data = {'Name': ['Amara', 'Yulia', 'Charlie'],
#        'Age': ['24', '27', '22'],
#        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}
#df = pd.DataFrame(data)

## Convert 'Age' column to integers
#df['Age'] = df['Age'].astype(int)

## Convert 'JoinDate' column to datetime
#df['JoinDate'] = pd.to_datetime(df['JoinDate'])

#print(df.dtypes)  # Verify data types
#print(df)



#data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [23, 27, 32, 44]}
#df = pd.DataFrame(data)

## Slice 1
#subset_loc = df.loc[0:2, ['Name']]
#print(subset_loc)
## Slice 2
#subset_iloc = df.iloc[0:2, ]
#print(subset_iloc)


## Group data by a column and calculate the sum
#data = {'Category': ['A', 'B', 'A', 'B', 'C'],
#        'Values': [10, 20, 30, 40, 50]}
#df = pd.DataFrame(data)

## Group by 'Category' and calculate the sum
#grouped = df.groupby('Category').sum()
#print(grouped) # grouped is another DataFrame with summary data

## Calculate the mean for each group
#mean_values = df.groupby('Category')['Values'].mean()
#print(mean_values)

## Group by 'Category' and apply multiple aggregation functions
#result = df.groupby('Category').agg({'Values': ['sum', 'mean', 'count']})
#print(result)

#result1 = df.groupby('Category').agg({'Values': ['sum']})
#print(result1)
## or
#result2 = df.groupby('Category').agg({'Values': ['sum', 'mean', 'count']})
#print(result2)

## Join DataFrames by index
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']}, index=[1, 2, 3])
df2 = pd.DataFrame({'Score': [85, 92, 88]}, index=[1, 2, 4])

joined_df = df1.join(df2, how='outer')
print(joined_df)

#--------------------
joined_df['bogus']=['x','y','z','w'] # adds a column
print(joined_df)
joined_df['bogus']=joined_df['bogus'] + "_value"  # replaces a column
print(joined_df)
joined_df.drop('bogus', axis=1, inplace=True) # deletes the column.  You need axis=1 to identify that the drop is for a column, not a row
print(joined_df)

joined_df['bogus2']=['x','y','z'] # adds a column
print(joined_df)
joined_df['bogus']=joined_df['bogus'] + "_value"  # replaces a column
print(joined_df)
joined_df.drop('bogus', axis=1, inplace=True) # deletes the column.  You need axis=1 to identify that the drop is for a column, not a row
print(joined_df)