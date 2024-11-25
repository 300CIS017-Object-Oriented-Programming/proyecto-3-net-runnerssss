class ProgramaAcademico:
    def __init__(self):
        self._codigo_snies_del_programa = ""
        self._programa_academico = ""
        self._id_nivel_academico = ""
        self._nivel_academico = ""
        self._id_nivel_de_formacion = ""
        self._nivel_de_formacion = ""
        self._id_metodologia = ""
        self._metodologia = ""
        self._id_area = ""
        self._area_de_conocimiento = ""
        self._id_nucleo = ""
        self._nucleo_basico_del_conocimiento_nbc = ""
        self._id_cine_campo_amplio = ""
        self._desc_cine_campo_amplio = ""
        self._id_cine_campo_especifico = ""
        self._desc_cine_campo_especifico = ""
        self._id_cine_codigo_detallado = ""
        self._desc_cine_codigo_detallado = ""
        self._codigo_del_departamento_programa = ""
        self._departamento_de_oferta_del_programa = ""
        self._codigo_del_municipio_programa = ""
        self._municipio_de_oferta_del_programa = ""

    # Métodos getter y setter
    @property
    def codigo_snies_del_programa(self):
        return self._codigo_snies_del_programa

    @codigo_snies_del_programa.setter
    def codigo_snies_del_programa(self, value):
        self._codigo_snies_del_programa = value

    @property
    def programa_academico(self):
        return self._programa_academico

    @programa_academico.setter
    def programa_academico(self, value):
        self._programa_academico = value

    @property
    def id_nivel_academico(self):
        return self._id_nivel_academico

    @id_nivel_academico.setter
    def id_nivel_academico(self, value):
        self._id_nivel_academico = value

    @property
    def nivel_academico(self):
        return self._nivel_academico

    @nivel_academico.setter
    def nivel_academico(self, value):
        self._nivel_academico = value

    @property
    def id_nivel_de_formacion(self):
        return self._id_nivel_de_formacion

    @id_nivel_de_formacion.setter
    def id_nivel_de_formacion(self, value):
        self._id_nivel_de_formacion = value

    @property
    def nivel_de_formacion(self):
        return self._nivel_de_formacion

    @nivel_de_formacion.setter
    def nivel_de_formacion(self, value):
        self._nivel_de_formacion = value

    @property
    def id_metodologia(self):
        return self._id_metodologia

    @id_metodologia.setter
    def id_metodologia(self, value):
        self._id_metodologia = value

    @property
    def metodologia(self):
        return self._metodologia

    @metodologia.setter
    def metodologia(self, value):
        self._metodologia = value

    @property
    def id_area(self):
        return self._id_area

    @id_area.setter
    def id_area(self, value):
        self._id_area = value

    @property
    def area_de_conocimiento(self):
        return self._area_de_conocimiento

    @area_de_conocimiento.setter
    def area_de_conocimiento(self, value):
        self._area_de_conocimiento = value

    @property
    def id_nucleo(self):
        return self._id_nucleo

    @id_nucleo.setter
    def id_nucleo(self, value):
        self._id_nucleo = value

    @property
    def nucleo_basico_del_conocimiento_nbc(self):
        return self._nucleo_basico_del_conocimiento_nbc

    @nucleo_basico_del_conocimiento_nbc.setter
    def nucleo_basico_del_conocimiento_nbc(self, value):
        self._nucleo_basico_del_conocimiento_nbc = value

    @property
    def id_cine_campo_amplio(self):
        return self._id_cine_campo_amplio

    @id_cine_campo_amplio.setter
    def id_cine_campo_amplio(self, value):
        self._id_cine_campo_amplio = value

    @property
    def desc_cine_campo_amplio(self):
        return self._desc_cine_campo_amplio

    @desc_cine_campo_amplio.setter
    def desc_cine_campo_amplio(self, value):
        self._desc_cine_campo_amplio = value

    @property
    def id_cine_campo_especifico(self):
        return self._id_cine_campo_especifico

    @id_cine_campo_especifico.setter
    def id_cine_campo_especifico(self, value):
        self._id_cine_campo_especifico = value

    @property
    def desc_cine_campo_especifico(self):
        return self._desc_cine_campo_especifico

    @desc_cine_campo_especifico.setter
    def desc_cine_campo_especifico(self, value):
        self._desc_cine_campo_especifico = value

    @property
    def id_cine_codigo_detallado(self):
        return self._id_cine_codigo_detallado

    @id_cine_codigo_detallado.setter
    def id_cine_codigo_detallado(self, value):
        self._id_cine_codigo_detallado = value

    @property
    def desc_cine_codigo_detallado(self):
        return self._desc_cine_codigo_detallado

    @desc_cine_codigo_detallado.setter
    def desc_cine_codigo_detallado(self, value):
        self._desc_cine_codigo_detallado = value

    @property
    def codigo_del_departamento_programa(self):
        return self._codigo_del_departamento_programa

    @codigo_del_departamento_programa.setter
    def codigo_del_departamento_programa(self, value):
        self._codigo_del_departamento_programa = value

    @property
    def departamento_de_oferta_del_programa(self):
        return self._departamento_de_oferta_del_programa

    @departamento_de_oferta_del_programa.setter
    def departamento_de_oferta_del_programa(self, value):
        self._departamento_de_oferta_del_programa = value

    @property
    def codigo_del_municipio_programa(self):
        return self._codigo_del_municipio_programa

    @codigo_del_municipio_programa.setter
    def codigo_del_municipio_programa(self, value):
        self._codigo_del_municipio_programa = value

    @property
    def municipio_de_oferta_del_programa(self):
        return self._municipio_de_oferta_del_programa

    @municipio_de_oferta_del_programa.setter
    def municipio_de_oferta_del_programa(self, value):
        self._municipio_de_oferta_del_programa = value

    def imprimir(self):
        print(f"Código SNIES del Programa: {self._codigo_snies_del_programa}")
        print(f"Programa Académico: {self._programa_academico}")
        print(f"ID Nivel Académico: {self._id_nivel_academico}")
        print(f"Nivel Académico: {self._nivel_academico}")
        print(f"ID Nivel de Formación: {self._id_nivel_de_formacion}")
        print(f"Nivel de Formación: {self._nivel_de_formacion}")
        print(f"ID Metodología: {self._id_metodologia}")
        print(f"Metodología: {self._metodologia}")
        print(f"ID Área: {self._id_area}")
        print(f"Área de Conocimiento: {self._area_de_conocimiento}")
        print(f"ID Núcleo: {self._id_nucleo}")
        print(f"Núcleo Básico del Conocimiento: {self._nucleo_basico_del_conocimiento_nbc}")
        print(f"ID Cine Campo Amplio: {self._id_cine_campo_amplio}")
        print(f"Descripción Cine Campo Amplio: {self._desc_cine_campo_amplio}")
        print(f"ID Cine Campo Específico: {self._id_cine_campo_especifico}")
        print(f"Descripción Cine Campo Específico: {self._desc_cine_campo_especifico}")
        print(f"ID Cine Código Detallado: {self._id_cine_codigo_detallado}")
        print(f"Descripción Cine Código Detallado: {self._desc_cine_codigo_detallado}")
        print(f"Código del Departamento del Programa: {self._codigo_del_departamento_programa}")
        print(f"Departamento de Oferta del Programa: {self._departamento_de_oferta_del_programa}")
        print(f"Código del Municipio del Programa: {self._codigo_del_municipio_programa}")
        print(f"Municipio de Oferta del Programa: {self._municipio_de_oferta_del_programa}")
        print("-----------------------------------")
