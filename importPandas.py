import pandas

data = {
  'Motos': ["Suzuki", "Yamaha", "Kawazaki"], 
  'Registros': [3, 7, 2]
}

x = pandas.DataFrame(data)

print(x)
print(type(x))
print(type(pandas))
print(type(data))
