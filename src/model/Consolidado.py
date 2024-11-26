import streamlit as st
import pandas as pd
from datetime import datetime
from src.util.Settings import Settings


def procesar_rango_anios(start_year, end_year, settings):
    """
    Procesa los archivos Excel para el rango de años especificado.

    Args:
        start_year (int): Año inicial
        end_year (int): Año final
        settings (Settings): Objeto de configuración con las rutas base y columnas

    Returns:
        pandas.DataFrame: DataFrame combinado y procesado
    """
    dfs = []

    # Obtener las columnas desde settings
    columnas = settings.get_columns()

    for anio in range(start_year, end_year + 1):
        ruta_admitidos = f"{settings.files['admitidos']}{anio}.xlsx"

        # Leer el archivo del año actual con las columnas definidas en settings
        df_anio = leer_excel(ruta_admitidos, columnas)

    # Combinar todos los DataFrames
    if dfs:
        df_combinado = pd.concat(dfs, ignore_index=True)
        # Filtrar duplicados del DataFrame combinado
        df_final = filtrar_duplicados(df_combinado)
        return df_final
    return None


def filtros(controlador):
    # Configuración de la página
    st.set_page_config(page_title="Selector de Rango de Años", layout="wide")

    # Título de la aplicación
    st.title("Selector de Rango de Años")

    # Creamos dos columnas para los selectores
    col1, col2 = st.columns(2)

    with col1:
        # Selector para el año inicial
        start_year = st.number_input(
            "Año inicial",
            min_value=2000,
            max_value=2023,
            value=2020,
            step=1
        )

    with col2:
        # Selector para el año final
        end_year = st.number_input(
            "Año final",
            min_value=2000,
            max_value=2023,
            value=2023,
            step=1
        )

    # Validación del rango
    if start_year > end_year:
        st.error("El año inicial no puede ser mayor que el año final")
        return

    st.success(f"Rango seleccionado: {start_year} - {end_year}")

    # Botón para procesar los datos
    if st.button("Procesar datos"):
        with st.spinner("Procesando datos..."):
            df_resultado = procesar_rango_anios(start_year, end_year, controlador)

            if df_resultado is not None:
                st.write("Datos procesados exitosamente:")
                st.dataframe(df_resultado)
            else:
                st.error("No se pudieron procesar los datos para el rango seleccionado")


def leer_excel(ruta_archivo, columnas=None):
    """
    Lee un archivo Excel seleccionando solo las columnas especificadas.
    """
    try:
        df = pd.read_excel(ruta_archivo, usecols=columnas)
        return df
    except FileNotFoundError:
        st.error(f"No se encontró el archivo en la ruta: {ruta_archivo}")
        return None
    except ValueError as ve:
        st.error(f"Error con las columnas especificadas: {str(ve)}")
        return None
    except Exception as e:
        st.error(f"Error al leer el archivo: {str(e)}")
        return None


def filtrar_duplicados(df):
    """
    Filtra las filas duplicadas basándose en las columnas especificadas.
    """
    if df is None:
        return None

    columnas_filtro = ['CÓDIGO SNIES DEL PROGRAMA', 'CÓDIGO DEL MUNICIPIO (PROGRAMA)']
    df_filtrado = df.drop_duplicates(subset=columnas_filtro, keep='first')
    return df_filtrado


if __name__ == "__main__":
    filtros(st.session_state.controlador)