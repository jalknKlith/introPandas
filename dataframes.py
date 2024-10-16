import pandas as pd 

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

#locate Row
print(df.loc[0])

#use a list of indexes
print(df.loc[[0, 1]])

#give each row a name
dfn = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(dfn)

#located named indexes
print(dfn.loc["day2"])
