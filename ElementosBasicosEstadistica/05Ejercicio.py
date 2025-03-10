#Obtener Media, mediana, moda, rango, varianza, 
# desviasion estandar con su tabla de frecuencias 
# del archivo housing, deberan de mostrarse en un 
# formato de tablas separado con sus elementos solicitados.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('ElementosBasicosEstadistica/housing.csv')
Variables = ['longitude','latitude','housing_median_age','total_rooms',
'total_bedrooms','population','households','median_income','median_house_value',
'ocean_proximity']

for variable in Variables:
    list = df[variable].tolist()