import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

proyecto1=pd.read_csv('/Users/leonardomaldonadoalcala/MALDONADO_ALCALA_LEONARDO_6IV8_ANALISIS_DE_DATOS/ElementosBasicosEstadistica/proyecto1.csv')
catalogo_sucursales=pd.read_csv('/Users/leonardomaldonadoalcala/MALDONADO_ALCALA_LEONARDO_6IV8_ANALISIS_DE_DATOS/ElementosBasicosEstadistica/Catalogo_sucursal.csv')

ventasTotales = proyecto1['ventas_tot'].sum()
print(f'Las ventas totales son de  = {ventasTotales}')
adeudados = (proyecto1['B_adeudo']== 'Con adeudo').sum()
noAdeudados = (proyecto1['B_adeudo']== 'Sin adeudo').sum()
print(f'Socios con adeudos = {adeudados}')
print(f'Socios sin adeudos = {noAdeudados}')
print(f'Porcentaje de adeudos = {adeudados/len(proyecto1)*100}%')
print(f'Porcentaje de no adeudos = {noAdeudados/len(proyecto1)*100}%')
tiempo = proyecto1['B_mes']
for fecha in tiempo.unique():
    plt.hist(proyecto1[tiempo == fecha]['ventas_tot'], bins=10, alpha=0.5, label=f' {fecha}')

plt.title('Histograma de ventas totales por mes')
plt.xlabel('Ventas totales')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
std_por_fecha = []
fechas = []

for fecha in tiempo.unique():
    std = proyecto1[tiempo == fecha]['pagos_tot'].std()
    std_por_fecha.append(std)
    fechas.append(fecha)
    
plt.figure(figsize=(12, 6))
plt.bar(fechas, std_por_fecha)
plt.title('Desviación estándar de ventas totales por periodo de tiempo')
plt.xlabel('Periodo de tiempo')
plt.ylabel('Desviación estándar')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()