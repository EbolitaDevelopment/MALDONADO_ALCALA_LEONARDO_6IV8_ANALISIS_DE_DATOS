import pandas as pd
##Programa que pregunte al usuario un rango de años y muestra en la pantalla una serie de datos de ventas 
# indexados por los años, antes y despues de aplicar un descuento

inicio = int(input('Introduce el año de ventas inicial: '))
fin = int(input('Introduce el año de ventas final: '))

ventas={}

for i in range(inicio,fin+1):
    ventas[i]=float(input('Introduce las ventas del año '+str(i)+ ': '))
    
ventas = pd.Series(ventas)
print('Ventas\n',ventas)
print('Ventas con descuento\n',ventas*0.9)