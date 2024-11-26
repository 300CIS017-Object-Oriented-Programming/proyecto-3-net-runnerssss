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
            'CÓDIGO DE LA INSTITUCIÓN',
            'IES_PADRE',
            'INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)',
            'PRINCIPAL O SECCIONAL',
            'ID SECTOR IES',
            'SECTOR IES',
            'ID CARACTER',
            'CARACTER IES',
            'CÓDIGO DEL DEPARTAMENTO (IES)',
            'DEPARTAMENTO DE DOMICILIO DE LA IES',
            'CÓDIGO DEL MUNICIPIO IES',
            'MUNICIPIO DE DOMICILIO DE LA IES',
            'CÓDIGO SNIES DEL PROGRAMA',
            'PROGRAMA ACADÉMICO',
            'ID NIVEL ACADÉMICO',
            'NIVEL ACADÉMICO',
            'ID NIVEL DE FORMACIÓN',
            'NIVEL DE FORMACIÓN',
            'ID METODOLOGÍA',
            'METODOLOGÍA',
            'ID ÁREA',
            'ÁREA DE CONOCIMIENTO',
            'ID NÚCLEO',
            'NÚCLEO BÁSICO DEL CONOCIMIENTO (NBC)',
            'ID CINE CAMPO AMPLIO',
            'DESC CINE CAMPO AMPLIO',
            'ID CINE CAMPO ESPECIFICO',
            'DESC CINE CAMPO ESPECIFICO',
            'ID CINE CODIGO DETALLADO',
            'DESC CINE CODIGO DETALLADO',
            'CÓDIGO DEL DEPARTAMENTO (PROGRAMA)',
            'DEPARTAMENTO DE OFERTA DEL PROGRAMA',
            'CÓDIGO DEL MUNICIPIO (PROGRAMA)',
            'MUNICIPIO DE OFERTA DEL PROGRAMA'
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