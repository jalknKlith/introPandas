import pandas as pd 

data = {
  "calorias": [420, 380, 390],
  "duracion": [50, 40, 45]
}

#cargar todos los datos en la tabla
df = pd.DataFrame(data)

#imprimir la tabla
print(df)

#imprimir la fila uno
print(df.loc[0])

#imprimir la fila uno, y dos
print(df.loc[[0, 1]])

#nombrar cada fila
dfn = pd.DataFrame(data, index = ["day1", "day2", "day3"])

#imprimir la tabla
print(dfn)

#localizar la duracion del dia dos
print(dfn.loc["day2"])
