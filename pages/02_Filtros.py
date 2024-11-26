import streamlit as st
import pandas as pd
from utils import filtrar_por_anio, filtrar_por_palabra, tipo_dato


def filtros(controlador):
    st.title("Filtros")

    tipo_filtro = st.radio(
        "Selecciona el tipo de filtro",
        ["Rango de Años", "Palabras Clave"]
    )

    if tipo_filtro == "Rango de Años":
        st.subheader("Filtrar por Año")
        anio = st.select_slider("Selecciona el año para filtrar",
                                options=["2020","2021", "2022", "2023"],
                                value="2021")
        archivo = st.session_state.archivo_subido
        df_filtrado = filtrar_por_anio(archivo, anio)

        if not df_filtrado.empty:
            st.success(f"Resultados encontrados para el año {anio}")
            st.dataframe(df_filtrado)
            tipo_dato(df_filtrado)
        else:
            st.warning(f"No se encontraron resultados para el año {anio}")

    else:
        st.subheader("Palabras Clave")
        entrada_usuario = st.text_input("Escribe la palabra para filtrar:")
        columna = st.text_input("Indica la columna a filtrar (por defecto: Nombre):",
                                value="Nombre")

        if entrada_usuario:
            archivo = st.session_state.archivo_subido
            df_filtrado = filtrar_por_palabra(archivo, entrada_usuario, columna)

            if not df_filtrado.empty:
                st.success(f"Resultados encontrados para: '{entrada_usuario}' en la columna '{columna}'")
                st.dataframe(df_filtrado)
                tipo_dato(df_filtrado)
            else:
                st.warning(f"No se encontraron resultados para: '{entrada_usuario}' en la columna '{columna}'")


filtros(st.session_state.controlador)