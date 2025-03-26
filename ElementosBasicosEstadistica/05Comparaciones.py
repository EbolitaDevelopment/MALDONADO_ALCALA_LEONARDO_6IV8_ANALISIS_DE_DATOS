import numpy as np
import matplotlib.pyplot as plt

#Crear semilla random para reproductibidad
np.random.seed(0)
#Vamos a buscar los parametros para una distribución
#media
media = 0
#Desviaciones estandar
sigma1=1
sigma2=2
sigma3=3
#Numero de muestras para el analisis
n_muestras=1000
#Datos distribuciones normales
data1=np.random.normal(media,sigma1,n_muestras)
data2=np.random.normal(media,sigma2,n_muestras)
data3=np.random.normal(media,sigma3,n_muestras)
#Graficar
plt.figure(figsize=(10,6))
#Para que sirve un histograma : muestra la frecuencia de los datos
#Vamos a cargar frecuencias a partir de una grafica de hisstograma
plt.hist(data1,bins=30,color='blue',density=True,label='Desviación Estandar = 1' ,alpha=0.5)
plt.hist(data2,bins=30,color='red',density=True,label='Desviación Estandar = 2' ,alpha=0.5)
plt.hist(data3,bins=30,color='green',density=True,label='Desviación Estandar = 3' ,alpha=0.5)

#a grafcar
plt.title('Comparación de distribuciones Normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0.1,color='black',linewidth=0.5, ls='--')
plt.axvline(0,color='black',linewidth=0.5, ls='--')
plt.legend()
plt.grid()
plt.show()