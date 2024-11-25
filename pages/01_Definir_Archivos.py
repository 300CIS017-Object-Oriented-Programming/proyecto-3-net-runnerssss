import streamlit as st
import os
import shutil

def definir_archivos(controlador):
    if "comprobante" not in st.session_state:
        st.session_state.comprobante = 0

    st.title("Definir Archivos")

    # Mostrar archivos existentes
    input_path = "inputs"

    files = os.listdir(input_path)
    if files:
        st.subheader("Archivos existentes:")
        for file in files:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(file)
            with col2:
                if st.button("Eliminar", key=f"del_{file}"):
                    try:
                        os.remove(os.path.join(input_path, file))
                        st.success(f"Archivo {file} eliminado correctamente.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al eliminar el archivo: {str(e)}")
    else:
        st.info("No hay archivos en la carpeta de entrada.")


    # Subir nuevo archivo
    st.subheader("Subir nuevo archivo")
    archivo = st.file_uploader("Selecciona un archivo para subir", type=["csv", "txt"])

    if archivo:
        try:
            # Guardar el archivo en ../inputs
            with open(os.path.join(input_path, archivo.name), "wb") as f:
                f.write(archivo.getbuffer())
            st.success(f"Archivo {archivo.name} subido correctamente.")
            st.session_state.archivo_subido = archivo
            st.session_state.comprobante = 1
        except Exception as e:
            st.error(f"Error al guardar el archivo: {str(e)}")

    # Botón para continuar
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("Continuar"):
            if st.session_state.comprobante == 1:
                st.session_state.paso_actual += 1
                st.rerun()
            else:
                st.warning("Por favor, sube al menos un archivo antes de continuar.")


definir_archivos(st.session_state.controlador)