"""Calcularemos las distanicias entre todos los pares de puntos y determinaremos cuales están mas alejados entre si y cuales mas cercanos
utilizando las distancias euclidianas, manhattan y Chebyshev"""

import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos = {
    'Punto A':(2,3),
    'Punto B':(5,4),
    'Punto C':(1,1),
    'Punto D':(6,7),
    'Punto E':(3,5),
    'Punto F':(8,2),
    'Punto G':(4,6),
    'Punto H':(2,1)
}
#Convertir los puntos a un dataframe
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X','Y']
print('Coordenadas de los puntos:')
print(df_puntos)

def calcular_distancia(df_puntos):
    distancias  = pd.DataFrame(index=df_puntos.index,columns=df_puntos.index)
    #Callcular las distancias entre todos los pares de puntos
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i!=k:#No calcular la distancia entre el mismo punto
                distancias.loc[i,k]=distance.euclidean(df_puntos.loc[i],df_puntos.loc[k])
            else:
                distancias.loc[i,k]=0
    return distancias
distancias = calcular_distancia(df_puntos)
valor_maximo = distancias.values.max()
(punto1,punto2) = distancias.stack().idxmax()
print()
print('Tabla de distancias entre los puntos:')
print(distancias)
print()
print('La distancia maxima entre dos puntos es: ',valor_maximo)
print()
print('Los puntos mas alejados son: ',punto1,' y ',punto2)

#Otra manera de calcular la distancia maxima entre dos puntos
max_valor = distancias.max().max()
col_max = distancias.max().idxmax()
id_max=distancias[col_max].idxmax()
print()
print(f'Valor Máxima: {max_valor}')
print(f'Columna: {col_max}')
print(f'Indice: {id_max}')
#Hacer con manhattan y chebyshev
