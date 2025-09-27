import pandas as pd
import numpy as np

def cargar_datos(ruta_archivo):
    if ruta_archivo.endswith('.xlsx'):
        datos = pd.read_excel(ruta_archivo)
        df=pd.DataFrame(datos)
        print("Datos cargados exitosamente.")
        return df
    
    elif ruta_archivo.endswith('.csv'):
            datos = pd.read_csv(ruta_archivo)
            df=pd.DataFrame(datos)
            print("Datos cargados exitosamente.")
            return df
    
    elif ruta_archivo.endswith('.json'):
        datos = pd.read_json(ruta_archivo)
        df=pd.DataFrame(datos)
        print("Datos cargados exitosamente.")
        return df
    else:
        print("Formato de archivo no soportado. Por favor, use .xlsx o .csv o .json")
        return None
    

def limpiar_datos(datos):
    
    datos_limpios = datos.dropna()## Se eliminan filas con valores nulos, se toma esta decisión para simplificar ya que luego de la limpieza nos damos cuenta que son pocos los valores nulos
    datos_limpios = datos_limpios.drop_duplicates()
    
    
    print("Datos limpiados exitosamente.")
    return datos_limpios

def estandarizar_datos(datos):
    datos['nombre']=datos['nombre'].str.lower()
    datos['nombre']=datos['nombre'].str.strip()
    print("Datos estandarizados exitosamente.")
    return datos

def deleteSymbols(datos):
     datos['precio']=datos['precio'].str.replace('$','').astype(float)
     print("Función ejecutada correctamente")
     return datos



