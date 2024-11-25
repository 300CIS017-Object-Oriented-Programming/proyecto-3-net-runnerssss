from distutils.command.install import value

import streamlit as st
from streamlit import select_slider


def app():
        st.title("SNIES")
        st.write("Bienvenido a SNIES-Extractor, tu gestionador de confianza")

        st.header("Un poco acerca de SNIES ")
        url_video = "https://www.youtube.com/watch?v=dFmZbTBSMN4"
        st.video(url_video)

        st.header("¿Que deseas hacer?")
        url_imagen = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bioguia.com%2Ftendencias%2Fcuriosidad-cualidades-esenciales-tener-exito_35219107.html&psig=AOvVaw3AtYUwigUx8nx_MQ58nW3R&ust=1732590635459000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOivxbHB9okDFQAAAAAdAAAAABAE"
        st.image(url_imagen)

        if "comprobante" not in st.session_state:
                st.session_state.comprobante = 0
        eleccion = st.selectbox("Elige que se procede a hacer", ("Subir archivo", "Filtrar por año", "Filtrar por palabra", "Mostrar todo"))
        if eleccion == "Subir archivo":
                archivo = st.file_uploader("Selecciona un archivo para subir", type=["csv", "txt"])
                if archivo:
                        st.write("Archivo subido correctamente.")
                        st.session_state.comprobante = 1  # Actualizar comprobante
                else:
                        st.write("No se ha subido ningún archivo aún.")
        elif eleccion == "Filtrar por año":
                anio = st.select_slider("Selecciona el año para filtrar", options = ["2021","2022", "2023"], value = "2021")
                #se llama a la funcion filtrado por anio
                eleccion_archivo = st.selectbox("Desea usar el archivo subido o el de default", ("Subido", "Default"))
                if eleccion_archivo == "Subido":
                        if st.session_state.comprobante == 1:
                                print("funcion el archivo subido")
                        else:
                                st.error("No se ha subido algun archivo")

                elif eleccion_archivo == "Default":
                        print("funcion con el archivo de default")

        elif eleccion == "filtrar por palabra":
                st.subheader("Escribe la palabra para filtrar")
                entrada_usuario = st.text_input("Palabra: ")
                #se llama a la  funcion filtrado plabra
                eleccion_archivo = st.selectbox("Desea usar el archivo subido o el de default", ("Subido", "Default"))
                if eleccion_archivo == "Subido":
                        if st.session_state.comprobante== 1:
                                print("funcion el archivo subido")
                        else:
                                st.error("No se ha subido algun archivo")

                elif eleccion_archivo == "Default":
                        print("funcion con el archivo de default")
        elif eleccion == "Mostrar todo":
                print("se muestra todo")

