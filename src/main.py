
import Escritura
from Settings import Settings
import streamlit as st
import pandas as pd
<<<<<<< HEAD




def app():
    st.title("SNIES")
    st.write("Bienvenido a SNIES-Extractor, tu gestionador de confianza")

    st.header("Un poco acerca de SNIES")
    url_video = "https://www.youtube.com/watch?v=dFmZbTBSMN4"
    st.video(url_video)


        

    st.header("¿Qué deseas hacer?")
    url_imagen = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bioguia.com%2Ftendencias%2Fcuriosidad-cualidades-esenciales-tener-exito_35219107.html&psig=AOvVaw3AtYUwigUx8nx_MQ58nW3R&ust=1732590635459000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOivxbHB9okDFQAAAAAdAAAAABAE"
    st.image(url_imagen)

    if "comprobante" not in st.session_state:
        st.session_state.comprobante = 0
    eleccion = st.selectbox("Elige qué se procede a hacer", ("Subir archivo", "Filtrar por año", "Filtrar por palabra", "Mostrar todo", "Mostrar datos"))

    if eleccion == "Subir archivo":
        archivo = st.file_uploader("Selecciona un archivo para subir", type=["csv", "txt"])
        st.session_state.archivo_subido = archivo
        if archivo:
            st.success("Archivo subido correctamente.")
            st.session_state.comprobante = 1  # Actualizar comprobante
        else:
            st.write("No se ha subido ningún archivo aún.")

    elif eleccion == "Filtrar por año":
        anio = st.select_slider("Selecciona el año para filtrar", options=["2021", "2022", "2023"], value="2021")
        eleccion_archivo = st.selectbox("¿Desea usar el archivo subido o el de default?", ("Subido", "Default"))
        if eleccion_archivo == "Subido" and st.session_state.comprobante == 1:
            archivo = st.session_state.archivo_subido
            df_filtrado = filtrar_por_anio(archivo, anio)
            st.dataframe(df_filtrado)
            tipo_dato(df_filtrado)
        elif eleccion_archivo == "Default":
            st.error("Archivo default no implementado.")
        else:
            st.error("No se ha subido algún archivo.")

    elif eleccion == "Filtrar por palabra":
        entrada_usuario = st.text_input("Escribe la palabra para filtrar:")
        eleccion_archivo = st.selectbox("¿Desea usar el archivo subido o el de default?", ("Subido", "Default"))
        if eleccion_archivo == "Subido" and st.session_state.comprobante == 1:
            archivo = st.session_state.archivo_subido
            columna = st.text_input("Indica la columna a filtrar (por defecto: Nombre):", value="Nombre")
            df_filtrado = filtrar_por_palabra(archivo, entrada_usuario, columna)
            st.dataframe(df_filtrado)
            tipo_dato(df_filtrado)
        elif eleccion_archivo == "Default":
            st.error("Archivo default no implementado.")
        else:
            st.error("No se ha subido algún archivo.")

    elif eleccion == "Mostrar todo":
        if st.session_state.comprobante == 1:
            archivo = st.session_state.archivo_subido
            df = pd.read_csv(archivo)
            st.dataframe(df)
            tipo_dato(df)
        else:
            st.error("No se ha subido algún archivo.")

    elif eleccion == "Mostrar datos":
        eleccion_datos = st.selectbox("¿Qué datos deseas ver?", ("Carreras sin nuevos matriculados", "Porcentaje de aumento o descenso"))
        eleccion_archivo = st.selectbox("¿Desea usar el archivo subido o el de default?", ("Subido", "Default"))
        if eleccion_archivo == "Subido" and st.session_state.comprobante == 1:
            archivo = st.session_state.archivo_subido
            st.error("Función aún no implementada para 'Mostrar datos'.")
        elif eleccion_archivo == "Default":
            st.error("Archivo default no implementado.")
        else:
            st.error("No se ha subido algún archivo.")

def filtrar_por_anio(archivo, anio):
    df = pd.read_csv(archivo)
    df_filtrado = df[df['Año'] == int(anio)]
    return df_filtrado

def filtrar_por_palabra(archivo, palabra, columna='Nombre'):
    df = pd.read_csv(archivo)
    df_filtrado = df[df[columna].str.contains(palabra, na=False, case=False)]
    return df_filtrado

def exportar_datos(df, formato, nombre_archivo):
    if formato == "CSV":
        df.to_csv(f"{nombre_archivo}.csv", index=False)
    elif formato == "TXT":
        df.to_csv(f"{nombre_archivo}.txt", index=False, sep='\\t')
    elif formato == "JSON":
        df.to_json(f"{nombre_archivo}.json", orient="records", indent=2)

def tipo_dato(df):
    eleccion_escritura = st.selectbox("¿Desea exportarlo como escritura?", ("Si", "No"))
    if eleccion_escritura == "Si":
        eleccion_tipo_escritura = st.selectbox("¿Qué tipo de dato?", ("CSV", "TXT", "JSON"))
        nombre_archivo = st.text_input("Nombre del archivo para exportar (sin extensión):")
        if st.button("Exportar"):
            exportar_datos(df, eleccion_tipo_escritura, nombre_archivo)
            st.success(f"Archivo exportado como {eleccion_tipo_escritura}")
    else:
        st.success("Exportación omitida.")

app()

