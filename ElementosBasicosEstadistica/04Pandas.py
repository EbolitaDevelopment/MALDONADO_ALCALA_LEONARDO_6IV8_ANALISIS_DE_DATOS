import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#Mostrar primeras 5 filas
print(df.head())
#Mpstrar ultimas 5 filas
print(df.tail())
#Mostrar fila en especifico
print(df.iloc[7])
#Mostar columna en especifico
print(df['ocean_proximity'])
#Obtener ,edia de la columna de cuartos
media_de_cuartos = df['total_rooms'].mean()
print(f'La media de los cuartos es : {media_de_cuartos}')

#mediana
mediana_de_cuartos = df['total_rooms'].median()
print(f'La mediana de los cuartos es : {mediana_de_cuartos}')

#mediana
Sumatoria = df['population'].sum()
print(f'El salario total es de : {Sumatoria}')

#Filtar
filtado =df[df['ocean_proximity']=='ISLAND']
print(filtado)

#GraficarDispersion
plt.scatter(df['ocean_proximity'][:10],df['median_house_value'][:10])
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafica de dispersion de Proximidad al mar vs Precio')
plt.show()
