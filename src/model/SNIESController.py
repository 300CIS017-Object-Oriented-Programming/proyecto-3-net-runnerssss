import pandas as pd
from src.model.Escritura import LecturaXLSX
from src.util.Settings import Settings


class ControladorSNIES:
    def __init__(self):
        self.data_principal = pd.DataFrame()
        self.lector_xlsx = LecturaXLSX()
        self.encabezados_columnas = []
        self.paths = Settings()

    def manejar_datos(self, inicio, fin, filtro):
        try:
            anio_inicio = int(inicio)
            anio_fin = int(fin)
            rango_anios = list(range(min(anio_inicio, anio_fin), max(anio_inicio, anio_fin) + 1))

            primero = True
            lector_archivos = LecturaXLSX()

            for anio in rango_anios:
                rutas_archivos = [
                    self.paths.files['admitidos'],
                    self.paths.files['graduados'],
                    self.paths.files['inscritos'],
                    self.paths.files['matriculados'],
                    self.paths.files['matriculados_primer']
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