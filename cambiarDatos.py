import pandas as pd

#cargar el archivo csv
df = pd.read_csv('fechas.csv')

#cambiar duracion a 120 si es mayor a 120
for x in df.index:
  if df.loc[x, "Duracion"] > 120:
    df.loc[x, "Duracion"] = 120

#elimminar filas si 
for x in df.index: 
  if df.loc[x, "Calorias"] > 400:
    df.drop(x, inplace = True)

#imprimir tabla entera
print(df.to_string())

print(df.duplicated())