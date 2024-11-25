from typing import List
from src.model.ProgramaAcademico import ProgramaAcademico
from src.model.DatosInstitucion import DatosInstitucion
from src.model.Consolidado import Consolidado

class UnionDatos:
    def __init__(self):
        self._programa = ProgramaAcademico
        self._institucion = DatosInstitucion
        self._consolidados: List[Consolidado] = []
        
    @property
    def getPrograma(self):
        return self.programa
    
    @getPrograma.setter
    def getPrograma(self, value):
        self._programa = value
    
    @property
    def getInstitucion(self):
        return self._institucion
    
    @getInstitucion.setter
    def getInstitucion(self, value):
        self._institucion = value
    
    @property
    def get_consolidados(self):
        return self._consolidados
    
    @get_consolidados.setter
    def get_consolidados(self, lista):
        self._consolidados = lista
    

    def imprimir(self):
        if self._programa:
            self.programa.imprimir()
        if self.institucion:
            self.institucion.imprimir()
        for consolidado in self.consolidados:
            if consolidado:
                consolidado.imprimir()