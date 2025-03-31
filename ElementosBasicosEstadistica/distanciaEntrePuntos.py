import numpy as np
import pandas as pd
from scipy.spatial import distance

tiendas = {
    'TiendaA':(1,1),
    'TiendaB':(1,5),
    'TiendaC':(7,1),
    'TiendaD':(3,3),
    'TiendaE':(4,8),
}
#Convertit las coordenadas a un dataframe
df_tiendas = pd.DataFrame(tiendas).T
df_tiendas.columns = ['X','Y']
print('Coordenadas de las tiendas:')
print(df_tiendas)

distancias_ou=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)

for i in df_tiendas.index:
    for j in df_tiendas.index:
        distancias_ou.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        distancias_mh.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        distancias_ch.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])

print()
print('Distancias euclidianas de las tiendas:')
print(distancias_ou)
print()
print('Distancias manhattan de las tiendas:')
print(distancias_mh)
print()
print('Distancias Chebyshev las tiendas:')
print(distancias_ch)
