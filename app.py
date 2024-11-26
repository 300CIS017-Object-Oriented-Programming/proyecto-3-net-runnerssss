from src.model.SNIESController import ControladorSNIES
import streamlit as st
import os

def iniciar_programa():

    # Asigna el controlador como variable de instancia y en session_state para persistencia
    if 'controlador' not in st.session_state:
        st.session_state.controlador = ControladorSNIES()

    st.set_page_config(page_title="SNIES-Extractor", page_icon="📊️", layout="wide",
                       initial_sidebar_state="expanded")

    st.title("SNIES")
    st.header("Bienvenido a SNIES-Extractor, tu gestionador de confianza")
    pestana1, pestana2, pestana3 = st.tabs(["🏠 Inicio ", "📤 Subir Archivos", "📊 Ver Datos"])

    DIRECCION_INPUTS = r"C:\Users\juanj\Desktop\J.J trabajos\U\Tercer semestre\proyecto-3-net-runnerssss\src\docs\inputs>"

    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    with pestana1:
        col1, col2 = st.columns([1, 1])

        # Columna 1: Video de YouTube
        with col1:
            url_video = "https://www.youtube.com/watch?v=dFmZbTBSMN4"
            st.video(url_video)

        # Columna 2: Texto y foto
        with col2:
            st.subheader("¿Qué es SNIES?")
            st.write("""
                        El Sistema Nacional de Información de la Educación Superior (SNIES) es una plataforma administrada 
                        por el Ministerio de Educación Nacional de Colombia, cuyo objetivo es ofrecer información confiable 
                        y actualizada sobre los programas de educación superior en el país. Esta base de datos agrupa información 
                        clave sobre instituciones, programas académicos, estudiantes, y procesos académicos en todas las universidades, 
                        técnicos y tecnológicos de Colombia. 

                        Entre sus principales utilidades se encuentra la posibilidad de acceder a datos sobre la oferta educativa 
                        en diversas áreas de conocimiento, lo que facilita la toma de decisiones tanto para estudiantes que buscan 
                        opciones educativas, como para autoridades gubernamentales y académicas que necesitan información precisa 
                        para la formulación de políticas públicas. Además, el SNIES es esencial para el registro de los programas 
                        académicos y la acreditación de calidad educativa, lo que asegura que las instituciones cumplen con los 
                        estándares establecidos en el país.
                    """)

            # Agregar una imagen (puedes cambiar la URL por la de tu imagen local o URL externa)

        st.empty()
        # Fila de botones e ingreso del nombre
        col1, col2 = st.columns([1, 1])

        with col1:
            # Botón de ingreso del nombre del usuario
            user_name = st.text_input("Introduce tu nombre:", key="user_name")
            if st.button("Guardar Nombre"):
                if user_name:
                    st.session_state.user_name = user_name
                    st.success(f"Nombre guardado: {st.session_state.user_name}")
                else:
                    st.warning("Por favor ingresa un nombre.")
            if "user_name" in st.session_state:
                st.write(f"Nombre del usuario guardado: {st.session_state.user_name}")

        with col2:
                st.image("https://img.freepik.com/fotos-premium/buscando-pequena-intervencion-divina-toma-angulo-alto-grupo-estudiantes-universitarios-irreconocibles-orando-ayuda-sus-proximos-examenes_590464-7335.jpg?w=740", use_container_width =True)

        st.image("https://snies.mineducacion.gov.co/1778/channels-975_logo_snies.svg", use_container_width =True)

    with pestana2:
        st.header("Subir Archivos")
        st.markdown("### Carga tus archivos CSV o Excel para analizar los datos.")

        uploaded_file = st.file_uploader("Selecciona un archivo", type=["csv", "xlsx"])
        if uploaded_file:
            file_path = os.path.join(DIRECCION_INPUTS, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Archivo guardado correctamente: {file_path}")
        st.header("Archivos Subidos")

        # Obtener la lista de archivos en la carpeta
        files = os.listdir(DIRECCION_INPUTS)

        if files:
            st.markdown("### Archivos en la carpeta:")
            for file in files:
                st.markdown(f"- {file}")


if __name__ == "__main__":
    iniciar_programa()


iniciar_programa()

