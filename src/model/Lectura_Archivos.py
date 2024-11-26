import pandas as pd

def leer_excel(ruta_archivo, columnas=None):
    """
    Lee un archivo Excel seleccionando solo las columnas especificadas.
    Si alguna columna especificada no existe en el archivo, se omite sin generar error.

    Parámetros:
    ruta_archivo (str): Ruta del archivo Excel a leer
    columnas (list): Lista de columnas a leer. Si es None, lee todas las columnas.

    Retorna:
    DataFrame: DataFrame de pandas con las columnas encontradas, o None si hay un error.
    """
    try:
        # Primero leemos las columnas disponibles en el archivo
        todas_columnas = pd.read_excel(ruta_archivo, nrows=0).columns.tolist()

        if columnas is not None:
            # Filtrar solo las columnas que existen en el archivo
            columnas_validas = [col for col in columnas if col in todas_columnas]

            # Informar sobre las columnas que no se encontraron
            columnas_no_encontradas = [col for col in columnas if col not in todas_columnas]
            if columnas_no_encontradas:
                print(
                    f"Advertencia: Las siguientes columnas no se encontraron en el archivo y serán omitidas: {columnas_no_encontradas}")

            if not columnas_validas:
                print("Error: Ninguna de las columnas especificadas existe en el archivo.")
                print(f"Columnas disponibles en el archivo: {todas_columnas}")
                return None

            # Leer solo las columnas válidas
            df = pd.read_excel(ruta_archivo, usecols=columnas_validas)
        return df

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")
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
