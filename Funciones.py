import pandas as pd
import numpy as np

def cargar_datos(ruta_archivo):
    if ruta_archivo.endswith('.xlsx'):
        datos = pd.read_excel(ruta_archivo)
        print("Datos cargados exitosamente.")
        return datos
    
    elif ruta_archivo.endswith('.csv'):
            datos = pd.read_csv(ruta_archivo)
            print("Datos cargados exitosamente.")
            return datos
    
    elif ruta_archivo.endswith('.json'):
        datos = pd.read_json(ruta_archivo)
        print("Datos cargados exitosamente.")
        return datos
    else:
        print("Formato de archivo no soportado. Por favor, use .xlsx o .csv o .json")
        return None
    

def limpiar_datos(datos):
    if datos is None:
        print("No hay datos para limpiar.")
        return None
    
    datos_limpios = datos.dropna()## Se eliminan filas con valores nulos, se toma esta decisión para simplificar ya que luego de la limpieza nos damos cuenta que son pocos los valores nulos
    datos_limpios = datos_limpios.drop_duplicates()
    
    # Convertir tipos de datos si es necesario
    for columna in datos_limpios.select_dtypes(include=['object']).columns:
        try:
            datos_limpios[columna] = pd.to_numeric(datos_limpios[columna])
        except ValueError:
            pass  # No se puede convertir, dejar como está
    
    print("Datos limpiados exitosamente.")
    return datos_limpios