import os


class Settings:
    # Ruta base para los archivos
    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.inputs_dir = os.path.join(self.BASE_PATH, 'docs', 'inputs')
        self.outputs_dir = os.path.join(self.BASE_PATH, 'docs', 'outputs')
        self.files = {
            'admitidos': os.path.join(self.inputs_dir, 'admitidos'),
            'graduados': os.path.join(self.inputs_dir, 'graduados'),
            'inscritos': os.path.join(self.inputs_dir, 'inscritos'),
            'matriculados': os.path.join(self.inputs_dir, 'matriculados'),
            'matriculados_primer': os.path.join(self.inputs_dir, 'matriculadosprimersemestre')
        }

        # Columnas que se quieren leer de los archivos
        self.columns_to_read = [
            'Código de la Institución',
            'IES PADRE',
            'Institución de Educación Superior (IES)',
            'Principal o Seccional',
            'ID Sector IES',
            'Sector IES',
            'ID Caracter IES',
            'Caracter IES',
            'Código del departamento (IES)',
            'Departamento de domicilio de la IES',
            'Código del Municipio (IES)',
            'Municipio de domicilio de la IES'
        ]

        # Delimitador para archivos CSV
        self.DELIMITADOR = ';'
        self.COLUMNAS_INFO_CONSOLIDADOS = 8
        self.DATOS_ACADEM_DEMOGRAF = 4
        self.COLUMNA_13 = 13
        self.COLUMNA_12 = 12
        self.FILAS_RESTANTES = 3

    def get_output_path(self, filename):
        return os.path.join(self.outputs_dir, filename)

    def get_columns(self):
        return self.columns_to_read