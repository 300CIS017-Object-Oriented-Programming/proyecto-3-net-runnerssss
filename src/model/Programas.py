import pandas as pd
from src.util.Settings import Settings
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
        # print("\nPrimeras 5 filas del DataFrame con las columnas seleccionadas:")
        # print(df.head())
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


# Ejemplo de uso:
settings = Settings()
ruta_admitidos = settings.files['admitidos']+"2020.xlsx"
df = leer_excel(ruta_admitidos, columnas=settings.get_columns())