import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())

#imprimir que tipo de dato es
print(type(df))
print(type(pd))