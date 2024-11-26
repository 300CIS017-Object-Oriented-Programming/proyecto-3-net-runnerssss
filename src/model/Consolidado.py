import streamlit as st
import pandas as pd
import os
from datetime import datetime
from src.util.Settings import Settings
from src.model.Lectura_Archivos import leer_excel, filtrar_duplicados


def consolidar_datos_por_tipo(start_year: int, end_year: int, nombre_archivo: str) -> pd.DataFrame:
    """
    Consolida datos de varios años para un tipo de archivo específico.

    Args:
        start_year: Año inicial
        end_year: Año final
        nombre_archivo: Tipo de archivo ('inscritos' o 'admitidos')

    Returns:
        DataFrame consolidado
    """
    settings = Settings()
    dfs = []

    for year in range(start_year, end_year + 1):
        ruta_archivo = f"{settings.files[nombre_archivo]}{year}.xlsx"
        try:
            df = leer_excel(ruta_archivo, settings.get_consolidados())
            df['AÑO'] = year
            dfs.append(df)
        except Exception as e:
            print(f"Error procesando archivo del año {year}: {str(e)}")

    if not dfs:
        raise ValueError("No se pudo procesar ningún archivo")

    return pd.concat(dfs, ignore_index=True)


def main():
    try:
        # Procesar datos de inscritos
        inscritos = consolidar_datos_por_tipo(2020, 2022, "inscritos")
        inscritos = filtrar_duplicados(inscritos)

        # Procesar datos de admitidos
        admitidos = consolidar_datos_por_tipo(2020, 2022, "admitidos")
        admitidos = filtrar_duplicados(admitidos)

        # Verificar tipos de datos antes del merge
        print("\nTipos de datos en inscritos:")
        print(inscritos.dtypes)
        print("\nTipos de datos en admitidos:")
        print(admitidos.dtypes)

        # Combinar datos
        merged_df = pd.merge(
            inscritos,
            admitidos,
            on=['CÓDIGO SNIES DEL PROGRAMA', 'CÓDIGO DEL MUNICIPIO (PROGRAMA)'],
            suffixes=('_inscritos', '_admitidos')
        )

        # Mostrar resultados
        print("\nDatos consolidados:")
        print(merged_df)

        return merged_df

    except Exception as e:
        print(f"Error en el procesamiento: {str(e)}")
        return None


if __name__ == "__main__":
    main()