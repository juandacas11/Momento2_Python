import pandas as pd
import numpy as np
from Funciones import *  # Importar las funciones desde el módulo de fun

datos_1 =cargar_datos('Data/productos.csv')
datos_2 =cargar_datos('Data/productos.json')
datos_3 =cargar_datos('Data/ventas.csv')
datos_1_limpios = limpiar_datos(datos_1)
datos_2_limpios = limpiar_datos(datos_2)

datos_1_estandarizados = estandarizar_datos(datos_1_limpios)
datos_2_estandarizados = estandarizar_datos(datos_2_limpios)

datos_1_final=deleteSymbols(datos_1_estandarizados)

#imprimir en consola los primeros 5 registros del primer conjunto de datos estandarizados
print("Primeros 5 registros del primer conjunto de datos estandarizados:")
print(datos_1_estandarizados.head())


##Imprimir en consola ventas mayores a 5 unidades
print("---------------- Ventas mayores a 5 unidades --------------------")
print(datos_3[datos_3['cantidad'] > 5])


##Imprimir en consola por agrupaciones (Groupby) 
print("-------------------Unidades por Caegoria------------------------")
print(datos_1_final.groupby('categoria')['precio'].count())



print("-------------------Tabla Total------------------------")
print(pd.merge(datos_3, datos_1_final, on='producto_id', how='inner'))
