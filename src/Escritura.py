import pandas as pd

class Lectura:
    
    def generar_archivo(self, ruta_archivo: str, datos: pd.DataFrame) -> bool:
        raise NotImplementedError


class GestorCSV(Lectura):
    
    def generar_archivo(self, ruta_archivo: str, datos: pd.DataFrame) -> bool:
        try:
            datos.to_csv(ruta_archivo, index=False, encoding='utf-8')  # Guardar como CSV
            return True
        except Exception as error:
            print(f"Error al guardar el archivo CSV: {error}")
            return False


class LecturaJSON(Lectura):
    
    def generar_archivo(self, ruta_archivo: str, datos: pd.DataFrame) -> bool:
        try:
            datos.to_json(ruta_archivo, orient='records', indent=4, force_ascii=False)  # Guardar como JSON
            return True
        except Exception as error:
            print(f"Error al guardar el archivo JSON: {error}")
            return False


class LecturaXLSX(Lectura):
    
    @staticmethod
    def procesar_excel(ruta_archivo, filtro, solo_columna_clave):
        try:
            datos = pd.read_excel(ruta_archivo, header=None)

            # Limpiar filas completamente vacías
            datos.dropna(how='all', inplace=True)

            # Buscar encabezado relevante
            indice_encabezado = None
            for i, fila in datos.iterrows():
                if "PROGRAMA ACADÉMICO" in fila.values:
                    indice_encabezado = i
                    break

            if indice_encabezado is None:
                raise KeyError("No se identificó la columna clave 'PROGRAMA ACADÉMICO'.")

            # Leer el archivo con el encabezado encontrado
            datos = pd.read_excel(ruta_archivo, header=indice_encabezado)
            datos.columns = datos.columns.str.strip().str.upper()

            if "PROGRAMA ACADÉMICO" not in datos.columns:
                raise KeyError("Falta la columna 'PROGRAMA ACADÉMICO' después de procesar.")

            # Filtrar por palabra clave
            datos_filtrados = datos[datos["PROGRAMA ACADÉMICO"].str.contains(filtro, case=False, na=False)]

            columnas_requeridas = [
                "CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE"
            ] if solo_columna_clave else [
                "CÓDIGO SNIES DEL PROGRAMA", "METODOLOGÍA", "PROGRAMA ACADÉMICO",
                "INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)", "PRINCIPAL O SECCIONAL",
                "DEPARTAMENTO DE OFERTA DEL PROGRAMA", "MUNICIPIO DE OFERTA DEL PROGRAMA",
                "NIVEL DE FORMACIÓN", "SEMESTRE"
            ]

            # Agrupar y consolidar información
            ultima_columna = datos.columns[-1]
            combinados = datos_filtrados[columnas_requeridas]
            combinados = pd.concat([combinados, datos_filtrados[ultima_columna]], axis=1)

            resultado_final = combinados.groupby(columnas_requeridas).sum(numeric_only=True).reset_index()
            return resultado_final

        except Exception as error:
            print(f"Error al procesar el Excel: {error}")
            return None

    def generar_archivo(self, ruta_archivo: str, datos: pd.DataFrame) -> bool:
        try:
            datos.to_excel(ruta_archivo, index=False, engine='openpyxl')  # Guardar como Excel
            return True
        except Exception as error:
            print(f"Error al guardar el archivo Excel: {error}")
            return False
