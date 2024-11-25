import streamlit as st
import os


def definir_archivos(controlador):
    # Verificar si ya se inició el proceso
    if "comprobante" not in st.session_state:
        st.session_state.comprobante = 0

    # Si el comprobante es 1, mostrar mensaje de advertencia y no permitir cambios
    if st.session_state.comprobante == 1:
        st.warning("Debe terminar el proceso para cambiar los archivos que se van a revisar")
        st.stop()  # Detiene la ejecución del resto de la página

    st.title("Definir Archivos")

    # Mostrar archivos existentes
    input_path = "inputs"
    files = os.listdir(input_path)
    if files:
        st.subheader("Archivos existentes:")
        # Crear tabla simple con nombre y botón de eliminar
        for file in files:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(file)
            with col2:
                if st.button("Eliminar️", key=f"del_{file}"):
                    try:
                        os.remove(os.path.join(input_path, file))
                        st.success(f"Archivo {file} eliminado correctamente.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al eliminar el archivo: {str(e)}")
    else:
        st.info("No hay archivos en la carpeta de entrada.")

    # Subir nuevo archivo
    st.subheader("Subir Nuevo Archivo")
    archivo = st.file_uploader("Selecciona un archivo para subir", type=["xlsx"])
    if archivo:
        try:
            # Guardar el archivo en ../inputs
            with open(os.path.join(input_path, archivo.name), "wb") as f:
                f.write(archivo.getbuffer())
            st.success(f"Archivo {archivo.name} subido correctamente.")
            st.session_state.archivo_subido = archivo
        except Exception as e:
            st.error(f"Error al guardar el archivo: {str(e)}")

    # Agregar espacio antes del botón
    st.write("")
    st.write("")

    # Centrar el botón de continuar usando columnas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continuar", type="primary"):
            st.session_state.comprobante = 1
            # Redirigir a la página de filtros
            st.switch_page("pages/02_Filtros.py")


definir_archivos(st.session_state.controlador)