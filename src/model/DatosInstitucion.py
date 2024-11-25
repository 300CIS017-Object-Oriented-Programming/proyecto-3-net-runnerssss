class DatosInstitucion:
    def __init__(self):
        self._codigo_de_la_institucion = ""
        self._ies_padre = ""
        self._institucion_de_educacion_superior_ies = ""
        self._principal_o_seccional = ""
        self._id_sector_ies = ""
        self._sector_ies = ""
        self._id_caracter = ""
        self._caracter_ies = ""
        self._codigo_del_departamento_ies = ""
        self._departamento_de_domicilio_de_la_ies = ""
        self._codigo_del_municipio_ies = ""
        self._municipio_de_domicilio_de_la_ies = ""

    # Métodos getter y setter
    @property
    def codigo_de_la_institucion(self):
        return self._codigo_de_la_institucion

    @codigo_de_la_institucion.setter
    def codigo_de_la_institucion(self, value):
        self._codigo_de_la_institucion = value

    @property
    def ies_padre(self):
        return self._ies_padre

    @ies_padre.setter
    def ies_padre(self, value):
        self._ies_padre = value

    @property
    def institucion_de_educacion_superior_ies(self):
        return self._institucion_de_educacion_superior_ies

    @institucion_de_educacion_superior_ies.setter
    def institucion_de_educacion_superior_ies(self, value):
        self._institucion_de_educacion_superior_ies = value

    @property
    def principal_o_seccional(self):
        return self._principal_o_seccional

    @principal_o_seccional.setter
    def principal_o_seccional(self, value):
        self._principal_o_seccional = value

    @property
    def id_sector_ies(self):
        return self._id_sector_ies

    @id_sector_ies.setter
    def id_sector_ies(self, value):
        self._id_sector_ies = value

    @property
    def sector_ies(self):
        return self._sector_ies

    @sector_ies.setter
    def sector_ies(self, value):
        self._sector_ies = value

    @property
    def id_caracter(self):
        return self._id_caracter

    @id_caracter.setter
    def id_caracter(self, value):
        self._id_caracter = value

    @property
    def caracter_ies(self):
        return self._caracter_ies

    @caracter_ies.setter
    def caracter_ies(self, value):
        self._caracter_ies = value

    @property
    def codigo_del_departamento_ies(self):
        return self._codigo_del_departamento_ies

    @codigo_del_departamento_ies.setter
    def codigo_del_departamento_ies(self, value):
        self._codigo_del_departamento_ies = value

    @property
    def departamento_de_domicilio_de_la_ies(self):
        return self._departamento_de_domicilio_de_la_ies

    @departamento_de_domicilio_de_la_ies.setter
    def departamento_de_domicilio_de_la_ies(self, value):
        self._departamento_de_domicilio_de_la_ies = value

    @property
    def codigo_del_municipio_ies(self):
        return self._codigo_del_municipio_ies

    @codigo_del_municipio_ies.setter
    def codigo_del_municipio_ies(self, value):
        self._codigo_del_municipio_ies = value

    @property
    def municipio_de_domicilio_de_la_ies(self):
        return self._municipio_de_domicilio_de_la_ies

    @municipio_de_domicilio_de_la_ies.setter
    def municipio_de_domicilio_de_la_ies(self, value):
        self._municipio_de_domicilio_de_la_ies = value

    def imprimir(self):
        print(f"Código de la Institución: {self._codigo_de_la_institucion}")
        print(f"IES Padre: {self._ies_padre}")
        print(f"Institución de Educación Superior: {self._institucion_de_educacion_superior_ies}")
        print(f"Principal o Seccional: {self._principal_o_seccional}")
        print(f"ID Sector IES: {self._id_sector_ies}")
        print(f"Sector IES: {self._sector_ies}")
        print(f"ID Caracter: {self._id_caracter}")
        print(f"Caracter IES: {self._caracter_ies}")
        print(f"Código del Departamento: {self._codigo_del_departamento_ies}")
        print(f"Departamento de Domicilio: {self._departamento_de_domicilio_de_la_ies}")
        print(f"Código del Municipio: {self._codigo_del_municipio_ies}")
        print(f"Municipio de Domicilio: {self._municipio_de_domicilio_de_la_ies}")
        print("-----------------------------------")
