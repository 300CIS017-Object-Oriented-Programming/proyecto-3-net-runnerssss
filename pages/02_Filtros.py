import streamlit as st
import pandas as pd
from datetime import datetime
from src.model.Lectura_Archivos import leer_excel
from src.model.Lectura_Archivos import filtrar_duplicados
from src.util.Settings import Settings


def filtros(controlador):
    # Configuración de la página
    st.set_page_config(page_title="Selector de Rango de Años", layout="wide")

    # Título de la aplicación
    st.title("Selector de Rango de Años")

    # Obtenemos el año actual
    current_year = datetime.now().year

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
    else:
        st.success(f"Rango seleccionado: {start_year} - {end_year}")

        # Botón de continuar que solo aparece si el rango es válido
        if st.button("Continuar"):
            # Guardamos el rango en el controlador
            controlador.start_year = start_year
            controlador.end_year = end_year
            settings = Settings()
            ruta_inscritos = settings.files['inscritos'] + str(controlador.start_year) + ".xlsx"
            # Lee el archivo

            df = leer_excel(ruta_inscritos, columnas=settings.get_columns())
            # Aplica el filtro de duplicados
            df_filtrado = filtrar_duplicados(df)
            # Crear un contenedor expandible para mostrar el DataFrame
            st.dataframe(
                df_filtrado,
                width=None,  # Ancho automático
                height=500  # Altura fija de 500 píxeles
            )
# Ejecutar la función
filtros(st.session_state.controlador)