import pandas as pd

#Increase the maximum number of rows
#pd.options.display.max_rows = 200

df = pd.read_csv('data.csv')

#print the first 5 rows, the last 5 rows
print(df)

#print entire dataframe
#print(df.to_string())
print(type(df))
