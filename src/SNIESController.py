import pandas as pd
from Lectura import LecturaXlsx
from Settings import Settings


class ControladorSNIES:
    def __init__(self):
        self.data_principal = pd.DataFrame()  # DataFrame consolidado
        self.lector_xlsx = LecturaXlsx()
        self.encabezados_columnas = []
        self.ruta_admitidos = Settings.RUTA_ADMITIDOS
        self.ruta_graduados = Settings.RUTA_GRADUADOS
        self.ruta_inscritos = Settings.RUTA_INSCRITOS
        self.ruta_matriculados = Settings.RUTA_MATRICULADOS
        self.ruta_primera_matricula = Settings.RUTA_PRIMERA_MATRICULA

    def manejar_datos(self, inicio, fin, filtro):
        try:
            # Conversión y validación de años
            anio_inicio = int(inicio)
            anio_fin = int(fin)
            rango_anios = list(range(min(anio_inicio, anio_fin), max(anio_inicio, anio_fin) + 1))

            primero = True
            lector_archivos = LecturaXlsx()

            for anio in rango_anios:
                rutas_archivos = [
                    Settings.RUTA_ADMITIDOS,
                    Settings.RUTA_GRADUADOS,
                    Settings.RUTA_INSCRITOS,
                    Settings.RUTA_MATRICULADOS,
                    Settings.RUTA_PRIMERA_MATRICULA
                ]

                for ruta in rutas_archivos:
                    archivo_actual = f"{ruta}{anio}.xlsx"
                    data_reducida = lector_archivos.leer_archivo(archivo_actual, filtro, not primero)

                    data_reducida["COD_SNIES"] = data_reducida["CÓDIGO SNIES DEL PROGRAMA"].astype(str)
                    data_reducida["PERIODO"] = data_reducida["SEMESTRE"].astype(str)

                    if primero:
                        data_reducida.rename(columns={"ADMITIDOS": f'Admitidos_{anio}'}, inplace=True)
                        self.data = data_reducida
                        primero = False
                    else:
                        for columna in data_reducida.columns:
                            if columna not in ["COD_SNIES", "PERIODO"]:
                                data_reducida.rename(columns={columna: f'{columna}_{anio}'}, inplace=True)

                        self.data = pd.merge(
                            self.data, data_reducida,
                            on=["COD_SNIES", "PERIODO"],
                            how="left"
                        )

        except FileNotFoundError:
            raise FileNotFoundError("No se encontró alguno de los archivos necesarios para el procesamiento.")
        except Exception as error:
            raise Exception(f"Error procesando los datos: {error}")

        return self.data