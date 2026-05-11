import logging
from excepciones import ReservaInvalidaError, SoftwareFJError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "CREADA"

    def procesar(self, **parametros_dinamicos):
        try:
            if self.duracion <= 0:
                raise ReservaInvalidaError(f"La duración ({self.duracion}) es inválida.")
            
            total = self.servicio.calcular_costo(self.duracion, **parametros_dinamicos)
            self.estado = "CONFIRMADA"
            logging.info(f"ÉXITO: ID_Cliente {self.cliente.id_entidad} reservó {self.servicio.nombre}. Total: ${total}")
            return total

        except ReservaInvalidaError as e:
            self.estado = "CANCELADA POR ERROR"
            logging.error(f"Error en Reserva: {e}")
            raise
        except Exception as e:
            self.estado = "FALLO TÉCNICO"
            logging.critical(f"Fallo crítico inesperado: {e}")
            raise SoftwareFJError("El sistema de reservas colapsó internamente.") from e
        finally:
            print(f">>> Finalización de proceso. Estado: {self.estado}\n")