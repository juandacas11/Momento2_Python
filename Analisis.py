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



ventas=pd.merge(datos_3, datos_1_final, on='producto_id', how='inner')

conteo = ventas['producto_id'].value_counts()

# Obtener el producto_id con más registros
producto_mas_frecuente = conteo.idxmax()
cantidad = conteo.max()

print(f"El producto_id con más registros es {producto_mas_frecuente} con {cantidad} registros.")


# Convertir la columna de fecha a tipo datetime (ajusta el nombre de la columna si es necesario)
ventas['fecha'] = pd.to_datetime(ventas['fecha'])

# Filtrar ventas antes del 1 de marzo
ventas_filtradas = ventas[ventas['fecha'] < '2025-03-01']

# Agrupar y contar por categoría
conteo_por_categoria = ventas_filtradas.groupby('categoria').size()

print(conteo_por_categoria)