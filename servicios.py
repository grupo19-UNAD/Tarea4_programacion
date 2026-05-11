# servicios.py (Ajuste para lucirte con el profe)
from abc import ABC, abstractmethod
from excepciones import ValidacionDatosError


class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        if costo_base < 0:
            raise ValidacionDatosError("El costo base no puede ser negativo.")
        self.nombre = nombre
        self.costo_base = costo_base
        
    @abstractmethod
    def calcular_costo(self, cantidad, **kwargs):
        pass

    # Añadimos este método para fortalecer el Polimorfismo
    def __str__(self):
        return f"Servicio: {self.nombre} | Costo Base: ${self.costo_base}"

class SalaReunion(Servicio):
    def calcular_costo(self, horas, descuento=0):
        total = (self.costo_base * horas) - descuento
        return max(total, 0)

    def obtener_detalles(self):
        return f"SALA: {self.nombre} (Costo/Hora: ${self.costo_base})"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias, tiene_seguro=True):
        costo = self.costo_base * dias
        if tiene_seguro:
            costo += 25.0
        return costo

    def obtener_detalles(self):
        return f"EQUIPO: {self.nombre} (Costo/Día: ${self.costo_base})"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones):
        if sesiones >= 5:
            return (self.costo_base * sesiones) * 0.80
        return self.costo_base * sesiones

    def obtener_detalles(self):
        return f"ASESORÍA: {self.nombre} (Costo/Sesión: ${self.costo_base})"