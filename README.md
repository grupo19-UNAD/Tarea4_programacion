# Tarea4_programacion
tarea 4 curso de programacion 

Sistema de Gestión Software FJ

## Descripción del Proyecto
# 🚀 Proyecto Software FJ - Gestión de Servicios
Este proyecto es una solución integral diseñada para la gestión automatizada de servicios empresariales. El enfoque principal fue construir una aplicación **resiliente**, capaz de procesar operaciones masivas sin interrumpir su ejecución ante datos erróneos.

## 🛠️ Estructura del Proyecto
Siguiendo las recomendaciones docentes para fortalecer la organización, el sistema se ha dividido en los siguientes módulos independientes:

* **`excepciones.py`**: Definición de la jerarquía de errores personalizados (`SoftwareFJError`, `ValidacionDatosError`, `ReservaInvalidaError`).
* **`entidades.py`**: Contiene la clase abstracta `EntidadSistema` y la clase `Cliente` con validaciones de encapsulamiento.
* **`servicios.py`**: Implementación de la jerarquía de servicios (`SalaReunion`, `AlquilerEquipo`, `AsesoriaEspecializada`) aplicando herencia y polimorfismo.
* **`reserva.py`**: Módulo mediador que gestiona la lógica de reservas y el manejo de excepciones de negocio.
* **`main.py`**: Punto de entrada del programa que orquesta la simulación y configura el sistema de logs.

## 💎 Pilares POO e Innovaciones
* **Abstracción:** Uso de interfaces y clases base abstractas (ABC) para definir contratos de software claros.
* **Encapsulamiento:** Protección de datos sensibles en la clase `Cliente` mediante atributos privados y validaciones en el constructor.
* **Polimorfismo:** Implementación de métodos especializados de cálculo de costos y representación textual (`__str__`) en cada tipo de servicio.
* **Resiliencia (Manejo de Errores):** El sistema captura fallos en tiempo real y los registra en el archivo `software_fj.log`, permitiendo que la simulación de 10 operaciones continúe sin detenerse.

## 📋 Auditoría y Logs
Toda la actividad del sistema se almacena con codificación UTF-8 para garantizar la legibilidad de caracteres especiales:
* **Archivo:** `software_fj.log`
* **Niveles:** INFO para éxitos, ERROR para validaciones fallidas y CRITICAL para errores de sistema.

## 👥 Integrantes del Equipo
* **Desarrollo de Seguridad y Estructura:** Yareth Jimenez
* **Desarrollo de Lógica de Negocio:** Maria Celeste Aconcha