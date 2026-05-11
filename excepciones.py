
class SoftwareFJError(Exception):
    """Excepción raíz para el sistema Software FJ"""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los parámetros de una reserva son ilógicos"""
    pass

class ValidacionDatosError(SoftwareFJError):
    """Se lanza cuando un dato de cliente o servicio no cumple el formato"""
    pass