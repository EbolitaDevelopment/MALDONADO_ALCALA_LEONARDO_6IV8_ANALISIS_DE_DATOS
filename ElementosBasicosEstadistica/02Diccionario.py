import pandas as pd

#Hacer una funcion que reciba un diccionario 
# con las notas de los estudiantes del curso y 
# devuelva el diccionario con minimo y maxima media 
# desviación tipica

def estadisticas(notas):
    notas = pd.Series(notas)
    estadistica = pd.Series([notas.min(),notas.max(),notas.mean(),
    notas.std()],index=['Minimo','Maximo','Media','Desviacion Estandar'])
    return estadistica

notas = {'Juan':9,'Juanita':7,'Pedro':6.6,'Fabian':8.5,'Maximiliano':7.5,
         'Sandra':9.8,'Rosario':9}
print(estadisticas(notas))