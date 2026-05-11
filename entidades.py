from abc import ABC, abstractmethod
from excepciones import ValidacionDatosError

class EntidadSistema(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

class Cliente(EntidadSistema):
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente)
        if not nombre or len(nombre) < 3:
            raise ValidacionDatosError(f"Nombre inválido: '{nombre}'. Mínimo 3 caracteres.")
        if "@" not in email:
            raise ValidacionDatosError(f"Email inválido: '{email}'. Falta el símbolo @.")
            
        self.__nombre = nombre
        self.__email = email

    def __str__(self):
        return f"Cliente: {self.__nombre} (ID: {self.id_entidad})"