#Obtener Media, mediana, moda, rango, varianza, 
# desviasion estandar con su tabla de frecuencias 
# del archivo housing, deberan de mostrarse en un 
# formato de tablas separado con sus elementos solicitados.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Variables = ['longitude','latitude','housing_median_age','total_rooms',
'total_bedrooms', 'population','households','median_income','median_house_value']

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

def tablas_housing(df, Variables):
    estadisticas = pd.DataFrame(index=['Media', 'mediana', 'moda', 'rango', 'varianza', 'desviasion estandar'], columns=Variables)

    for variable in Variables:
        estadisticas[variable] = [
            df[variable].mean(),
            df[variable].median(),
            df[variable].mode()[0],  
            df[variable].max() - df[variable].min(),
            df[variable].var(),
            df[variable].std()
        ]

    print(estadisticas)

    frecuencias = {}
    for variable in Variables:
        frecuencias[variable] = pd.DataFrame({
            'Frecuencia': df[variable].value_counts(),
            'Frecuencia Relativa': df[variable].value_counts(normalize=True),
            'Frecuencia Absoluta': df[variable].value_counts().cumsum(),
            'Frecuencia Absoluta Relativa': df[variable].value_counts(normalize=True).cumsum()
        })
        print(f"*******************************************************************+\
******************************************************************************************\
          \nFRECUENCIAS PARA: {variable}:\n")
        print(frecuencias[variable])



Variable = ['total_bedrooms','population']

def graficas_housing(df, variables):
    fig, axes = plt.subplots(1, len(variables) + 1, figsize=(20, 6), sharey=True)
    colors = ['blue', 'orange', 'green']

    for i, variable in enumerate(variables):
        sns.histplot(df[variable], color=colors[i % len(colors)], kde=True, ax=axes[i])
        axes[i].set_title(f'Histograma de {variable}')
        axes[i].set_xlabel(variable)
        axes[i].axvline(df[variable].mean(), color='black', linestyle='dashed', linewidth=1, label='Media')
        
    sns.histplot(df['median_house_value'], color='red', kde=True, ax=axes[-1])
    axes[-1].set_title('Histograma de median_house_value')
    axes[-1].set_xlabel('median_house_value')
    axes[-1].axvline(df['median_house_value'].mean(), color='black', linestyle='dashed', linewidth=1, label='Media')

    plt.ylabel('Frecuencia')
    plt.show()
    
print(tablas_housing(df,  Variables))
graficas_housing(df,Variable)
