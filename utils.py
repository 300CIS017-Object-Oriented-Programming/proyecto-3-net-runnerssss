import pandas as pd

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
        df.to_csv(f"{nombre_archivo}.txt", index=False, sep='\t')
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