#importando pandas
import pandas as pd

#leyendo el archivo df= dataframe 
df = pd.read_csv('3-SEMI_AVANZADO/csv/archivo.csv')
df2 = pd.read_csv('3-SEMI_AVANZADO/csv/archivo.csv')

#obteniando los datos de una columna
nombres= df['nombre']

# Convirtiendo la columna 'age' a tipo numérico (entero)
#intenta convertir los valores a números y, si no puede, reemplaza esos valores con NaN (gracias al parámetro errors='coerce')
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')

#ordenando el df por la edad 
df_ordenado = df.sort_values('edad')
#print(df_ordenado)

#ordenando el df por la edad inverso
df_ordenado_inverso = df.sort_values('edad', ascending=False)
#print(df_ordenado_inverso)

#concatenando 2 data frames 
df_concat = pd.concat([df,df2])

#accediendo a las primeras filas 
primeras_df = df.head(3)

#accediendo a las ultimas filas 
ultimas_df = df.tail(3)

#accediuendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#obteniendo data estadistica deñ dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2 con loc
elemento_especifico_loc = df.loc[2,'edad']

#accediendo a una columna con loc
apellido_loc = df.loc[:,'apellido']

#accediendo a una fila con loc es igual que iloc
fila_loc = df.loc[3,:]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a una columna con iloc
apellido_iloc = df.iloc[:,1]

#accediendo a una fila con iloc
fila_iloc = df.iloc[3,:]

#accediendo a filas con edad mayor a 30
mayor_30_loc = df.loc[df['edad']>30,:]

#otra forma de convertir datos de una columna 
df['edad'] = df['edad'].astype(str)

#reemplazando dato 
df['apellido'].replace('Jontade','Rozehnal',inplace=True)

#eliminando filas con datos inexistentas
df = df.dropna()

#eliminando filas repetidas
df= df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv('3-SEMI_AVANZADO/csv/csv_limpio.csv ')






#
