import streamlit as st
import pandas as pd
from datetime import datetime


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

filtros(st.session_state.controlador)