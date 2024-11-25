import os
class Settings:
    # Ruta base para los archivos
    def __init__(self):
        self.BASE_PATH = os.getcwd()
        self.inputs_dir = os.path.join(self.BASE_PATH, 'docs', 'inputs')
        self.outputs_dir = os.path.join(self.BASE_PATH, 'docs', 'outputs')
        self.files = {
            'admitidos': os.path.join(self.inputs_dir, 'Admitidos'),
            'graduados': os.path.join(self.inputs_dir, 'Graduados'),
            'inscritos': os.path.join(self.inputs_dir, 'Inscritos'),
            'matriculados': os.path.join(self.inputs_dir, 'Matriculados'),
            'matriculados_primer': os.path.join(self.inputs_dir, 'Matriculados Primer Curso')
        }

        # Delimitador para archivos CSV
        DELIMITADOR = ';'
        COLUMNAS_INFO_CONSOLIDADOS = 8
        DATOS_ACADEM_DEMOGRAF = 4
        COLUMNA_13 = 13
        COLUMNA_12 = 12
        FILAS_RESTANTES = 3

    def get_output_path(self, filename):
        return os.path.join(self.outputs_dir, filename)
