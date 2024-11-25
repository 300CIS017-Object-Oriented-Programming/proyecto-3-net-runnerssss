class Consolidado:
    def __init__(self):
        self._id_sexo = ""
        self._sexo = ""
        self._ano = ""
        self._semestre = ""
        self._inscritos = ""
        self._admitidos = ""
        self._matriculados = ""
        self._matriculados_primer_semestre = ""
        self._graduados = ""

    # Métodos getter y setter
    @property
    def id_sexo(self):
        return self._id_sexo

    @id_sexo.setter
    def id_sexo(self, value):
        self._id_sexo = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, value):
        self._semestre = value

    @property
    def inscritos(self):
        return self._inscritos

    @inscritos.setter
    def inscritos(self, value):
        self._inscritos = value

    @property
    def admitidos(self):
        return self._admitidos

    @admitidos.setter
    def admitidos(self, value):
        self._admitidos = value

    @property
    def matriculados(self):
        return self._matriculados

    @matriculados.setter
    def matriculados(self, value):
        self._matriculados = value

    @property
    def matriculados_primer_semestre(self):
        return self._matriculados_primer_semestre

    @matriculados_primer_semestre.setter
    def matriculados_primer_semestre(self, value):
        self._matriculados_primer_semestre = value

    @property
    def graduados(self):
        return self._graduados

    @graduados.setter
    def graduados(self, value):
        self._graduados = value

    def imprimir(self):
        print(f"Sexo: {self._sexo}, Año: {self._ano}, Semestre: {self._semestre}, "
              f"Inscritos: {self._inscritos}, Admitidos: {self._admitidos}, "
              f"Matriculados: {self._matriculados}, Graduados: {self._graduados}, "
              f"Matriculados Primer Semestre: {self._matriculados_primer_semestre}")
