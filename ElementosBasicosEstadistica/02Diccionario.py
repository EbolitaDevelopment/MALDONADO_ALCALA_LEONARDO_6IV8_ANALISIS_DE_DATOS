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

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>=6].sort_values(ascending=False)

def Reprobados(notas):
    notas = pd.Series(notas)
    return aprobados.sort_values(ascending=False)

notas = {'Juan':5.9,'Juanita':5,'Pedro':6.6,'Fabian':8.5,'Maximiliano':7.5,
         'Sandra':9.8,'Rosario':9}

print(estadisticas(notas))
print(aprobados(notas))
