from src.model.SNIESController import ControladorSNIES
import streamlit as st

def iniciar_programa():

    # Asigna el controlador como variable de instancia y en session_state para persistencia
    if 'controlador' not in st.session_state:
        st.session_state.controlador = ControladorSNIES()

    st.set_page_config(page_title="SNIES-Extractor", page_icon="📊️", layout="wide",
                       initial_sidebar_state="expanded")
    st.title("SNIES")
    st.write("Bienvenido a SNIES-Extractor, tu gestionador de confianza")

    st.header("Un poco acerca de SNIES")
    url_video = "https://www.youtube.com/watch?v=dFmZbTBSMN4"
    st.video(url_video)


if __name__ == "__main__":
    iniciar_programa()


