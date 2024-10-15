import pandas as pd

#velocidades
vel = {"day1": 60, "day2": 70, "day3": 90}

#serie
x = pd.Series(vel, index = ["day1", "day2"])

print(x)
print(type(x))
print(type(vel))
