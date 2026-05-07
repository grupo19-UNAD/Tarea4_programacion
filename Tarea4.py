# SISTEMA SOFTWARE FJ
# Gestión de clientes, servicios y reservas
# Proyecto en Python sin base de datos

from abc import ABC, abstractmethod
import logging

import logging  # Importa el módulo para registrar eventos y errores en un archivo externo
from abc import ABC, abstractmethod  # Importa las herramientas para crear Clases Abstractas

# --- CONFIGURACIÓN DEL SISTEMA DE LOGS ---

# Configura el archivo donde se guardará el historial de errores sin detener la ejecución
logging.basicConfig(
    filename='software_fj.log',  # Nombre del archivo de destino
    level=logging.INFO,  # Nivel de detalle: INFO para eventos normales, ERROR para fallos
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato: Fecha - Tipo - Mensaje
)

# --- DEFINICIÓN DE EXCEPCIONES PERSONALIZADAS ---

class SoftwareFJError(Exception):  # Clase base para todas las excepciones del proyecto
    """Excepción raíz para el sistema Software FJ"""
    pass  # Indica que la clase no tiene métodos adicionales, solo hereda de Exception

class ReservaInvalidaError(SoftwareFJError):  # Excepción para errores en la lógica de reserva
    """Se lanza cuando los parámetros de una reserva son ilógicos"""
    pass

class ValidacionDatosError(SoftwareFJError):  # Excepción para errores de entrada de datos
    """Se lanza cuando un dato de cliente o servicio no cumple el formato"""
    pass

# --- CLASES BASE Y ABSTRACCIÓN ---

class EntidadSistema(ABC):  # Clase abstracta: no se pueden crear objetos "EntidadSistema" directamente
    """Representa cualquier objeto que posea una identificación única en el sistema"""
    def __init__(self, id_entidad):  # Constructor de la clase base
        self._id_entidad = id_entidad  # Atributo Protegido (Encapsulación básica)

    @property  # Decorador para crear un Getter (acceso controlado al atributo)
    def id_entidad(self):  # Método para leer el ID sin modificarlo directamente
        return self._id_entidad  # Retorna el valor protegido
    
## --- CLASE CLIENTE (ENCAPSULAMIENTO) ---
class Cliente(EntidadSistema):  # Herencia: Cliente extiende de EntidadSistema
    """Gestiona la información de los clientes con validaciones estrictas"""
    def __init__(self, id_cliente, nombre, email):  # Constructor del cliente
        super().__init__(id_cliente)  # Llama al constructor de EntidadSistema para asignar el ID
        
        # VALIDACIONES ROBUSTAS
        
        if not nombre or len(nombre) < 3:  # Verifica que el nombre no esté vacío y tenga longitud mínima
            raise ValidacionDatosError(f"Nombre inválido: '{nombre}'. Mínimo 3 caracteres.")  # Lanza excepción
        if "@" not in email:  # Validación simple de formato de correo
            raise ValidacionDatosError(f"Email inválido: '{email}'. Falta el símbolo @.")  # Lanza excepción
            
        self.__nombre = nombre  # Atributo Privado (Encapsulación estricta con doble guion bajo)
        self.__email = email    # Atributo Privado (No accesible desde fuera de la clase)

    def __str__(self):  # Sobrescritura del método especial para representar el objeto como texto
        return f"Cliente: {self.__nombre} (ID: {self.id_entidad})"  # Retorna cadena formateada

# --- CLASES DE SERVICIOS (POLIMORFISMO Y HERENCIA) ---

















