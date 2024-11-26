from src.model.SNIESController import ControladorSNIES
import streamlit as st
import plotly.express as px

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




    #Graficos para los datos luegos de ser analizados por la funcion de leer, reciben el dataframe
    """
    programas_disponibles = df["Programa"].unique()
    programas_seleccionados = st.multiselect("Selecciona los programas académicos", programas_disponibles, default=programas_disponibles[:2])

    categorias = ["Inscritos", "Admitidos", "Nuevos Matriculados", "Matrícula Total", "Graduados"]
    categoria_seleccionada = st.selectbox("Selecciona la categoría para analizar", categorias)

    # Filtrar los datos
    df_filtrado = df[df["Programa"].isin(programas_seleccionados)]
    st.subheader(f"Tendencias históricas de {categoria_seleccionada}")
    fig_line = px.line(
        df_filtrado, <--- dataframe
        x="Año",
        y=categoria_seleccionada,
        color="Programa",
        title=f"Tendencias de {categoria_seleccionada} por programa",
        markers=True
    )
    fig_line.update_layout(xaxis_title="Año", yaxis_title=categoria_seleccionada)
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader(f"Comparación entre programas: {categoria_seleccionada}")
    fig_bar = px.bar(
        df_filtrado,
        x="Programa",
        y=categoria_seleccionada,
        color="Año",
        barmode="group",
        title=f"Comparativa de {categoria_seleccionada} entre programas",
    )
    fig_bar.update_layout(xaxis_title="Programa", yaxis_title=categoria_seleccionada)
    st.plotly_chart(fig_bar, use_container_width=True)
    """

if __name__ == "__main__":
    iniciar_programa()


