"""Calcularemos las distancias entre todos los pares de puntos y determinaremos cuales están mas alejados entre si y cuales mas cercanos
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
# Convertir los puntos a un dataframe
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X','Y']
print('Coordenadas de los puntos:')
print(df_puntos)

def calcular_distancia_generica(df_puntos, metrica):
    """Función genérica para calcular distancias según la métrica especificada"""
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for k in df_puntos.index:
            if i != k:
                distancias.loc[i,k] = metrica(df_puntos.loc[i], df_puntos.loc[k])
            else:
                distancias.loc[i,k] = 0
    return distancias

def mostrar_resultados(distancias, nombre_metrica):
    """Función para mostrar resultados de manera consistente"""
    valor_maximo = distancias.values.max()
    punto1, punto2 = distancias.stack().idxmax()
    
    print(f'\nResultados para distancia {nombre_metrica}:')
    print('Tabla de distancias entre los puntos:')
    print(distancias)
    print(f'\nLa distancia máxima entre dos puntos es: {valor_maximo}')
    print(f'Los puntos más alejados son: {punto1} y {punto2}')

# Calcular y mostrar resultados para cada métrica
distancias_euclidean = calcular_distancia_generica(df_puntos, distance.euclidean)
distancias_manhattan = calcular_distancia_generica(df_puntos, distance.cityblock)
distancias_chebyshev = calcular_distancia_generica(df_puntos, distance.chebyshev)

mostrar_resultados(distancias_euclidean, "Euclidiana")
mostrar_resultados(distancias_manhattan, "Manhattan")
mostrar_resultados(distancias_chebyshev, "Chebyshev")