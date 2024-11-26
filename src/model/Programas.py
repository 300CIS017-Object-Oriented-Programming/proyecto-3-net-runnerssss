import pandas as pd
from src.util.Settings import Settings

from datetime import datetime
import os
def leer_excel(ruta_archivo, columnas=None):
    """
    Lee un archivo Excel seleccionando solo las columnas especificadas.
    Parámetros:
    ruta_archivo (str): Ruta del archivo Excel a leer
    columnas (list): Lista de columnas a leer
    nombre_hoja (str, opcional): Nombre de la hoja a leer
    """
    try:
        df = pd.read_excel(ruta_archivo, usecols=columnas)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")
        return None
    except ValueError as ve:
        print(f"Error con las columnas especificadas: {str(ve)}")
        print("Columnas disponibles en el archivo:", pd.read_excel(ruta_archivo).columns.tolist())
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return None
def filtrar_duplicados(df):
    """
    Filtra las filas duplicadas basándose en las columnas 'CÓDIGO SNIES DEL PROGRAMA'
    y 'CÓDIGO DEL DEPARTAMENTO (PROGRAMA)'.

    Parámetros:
    df (pandas.DataFrame): DataFrame a filtrar

    Retorna:
    pandas.DataFrame: DataFrame sin duplicados
    """
    if df is None:
        return None

    columnas_filtro = ['CÓDIGO SNIES DEL PROGRAMA', 'CÓDIGO DEL MUNICIPIO (PROGRAMA)']

    # Elimina duplicados manteniendo la primera ocurrencia
    df_filtrado = df.drop_duplicates(subset=columnas_filtro, keep='first')

    return df_filtrado




# # Ejemplo de uso:
# if __name__ == "__main__":
#     settings = Settings()
#     ruta_admitidos = settings.files['admitidos'] + "2020.xlsx"
#
#     # Lee el archivo
#     df = leer_excel(ruta_admitidos, columnas=settings.get_columns())
#
#     # Aplica el filtro de duplicados
#     df_filtrado = filtrar_duplicados(df)
