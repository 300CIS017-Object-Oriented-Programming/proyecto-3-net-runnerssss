from distutils.command.install import value
import Escritura
import streamlit as st
import pandas as pd
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
        eleccion = st.selectbox("Elige que se procede a hacer", ("Subir archivo", "Filtrar por año", "Filtrar por palabra", "Mostrar todo", "Mostrar datos"))
        if eleccion == "Subir archivo":
                archivo = st.file_uploader("Selecciona un archivo para subir", type=["csv", "txt"])
                st.session_state.archivo_subido = archivo
                if archivo:
                        st.success("Archivo subido correctamente.")
                        st.session_state.comprobante = 1  # Actualizar comprobante
                else:
                        st.write("No se ha subido ningún archivo aún.")
        elif eleccion == "Filtrar por año":
                anio = st.select_slider("Selecciona el año para filtrar", options = ["2021","2022", "2023"], value = "2021")
                #se llama a la funcion filtrado por anio
                eleccion_archivo = st.selectbox("Desea usar el archivo subido o el de default", ("Subido", "Default"))
                if eleccion_archivo == "Subido":
                        if st.session_state.comprobante == 1:
                                archivo = st.session_state.archivo_subido
                                print("funcion el archivo subido")
                                tipo_dato()#va el archivo
                        else:
                                st.error("No se ha subido algun archivo")

                elif eleccion_archivo == "Default":
                        print("funcion con el archivo de default")
                        tipo_dato()# va el archivo

        elif eleccion == "filtrar por palabra":
                st.subheader("Escribe la palabra para filtrar")
                entrada_usuario = st.text_input("Palabra: ")
                #se llama a la  funcion filtrado plabra
                eleccion_archivo = st.selectbox("Desea usar el archivo subido o el de default", ("Subido", "Default"))
                if eleccion_archivo == "Subido":
                        if st.session_state.comprobante== 1:
                                archivoa = st.session_state.archivo_subido
                                dx = pd.read_csv(archivoa)
                                st.write(f"Para buscarla escriba la palabra {entrada_usuario} en la lupa de la esquina superior derecha")
                                st.dataframe(dx)
                        else:
                                st.error("No se ha subido algun archivo")

                elif eleccion_archivo == "Default":
                        print("funcion con el archivo de default")
        elif eleccion == "Mostrar todo":
                print("se muestra todo")
                archivo = st.session_state.archivo_subido
                df = pd.read_csv(archivo)
                st.dataframe(df)
                #Falta el archivo base
        elif eleccion == "Mostrar datos":
                eleccion = st.selectbox("Que datos deseas ver", ("Carreras sin nuevos matriculados", "Porcentaje de aumento o desenso"))
                eleccion_archivo = st.selectbox("Desea usar el archivo subido o el de default", ("Subido", "Default"))
                if eleccion_archivo == "Subido":
                        if st.session_state.comprobante == 1:
                                archivo = st.session_state.archivo_subido
                                if eleccion == "Carreras sin nuevos matriculados":
                                        print("se utiliza la funcion con ese archivvo")
                                        tipo_dato()
                                elif eleccion == "Porcentaje de aumento o desenso":
                                        print("Igualmente")
                                        tipo_dato()
                        else:
                                st.error("No se ha subido algun archivo")

                elif eleccion_archivo == "Default":
                        if eleccion == "Carreras sin nuevos matriculados":
                                print("se utiliza la funcion con ese archivvo")
                                tipo_dato()
                        elif eleccion == "Porcentaje de aumento o desenso":
                                print("Igualmente")
                                tipo_dato()

def tipo_dato(archivo):
        eleccion_escritura = st.selectbox("Desea exportarlo como escritura",
                                          ("Si", "No"))
        if eleccion_escritura == "Si":
                eleccion_tipo_escritura = st.selectbox("¿Que tipo de dato?",
                                                       ("CVS", "TXT", "JSON"))
                if eleccion_tipo_escritura == "CVS":
                        print("funcion con el tipo de dato")
                elif eleccion_tipo_escritura == "TXT":
                        print("funcion con el tipo de dato")
                elif eleccion_tipo_escritura == "JSON":
                        print("funcion con el tipo de dato")
        else:
                st.success("Esta bien")
