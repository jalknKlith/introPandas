import pandas as pd

a = [1, 7, 2]

#nombrar las filas
b = pd.Series(a, index = ["x", "y", "z"])

print(b)
print(type(a))