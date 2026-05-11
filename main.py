# main.py
import logging
from entidades import Cliente
from servicios import SalaReunion, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ValidacionDatosError, ReservaInvalidaError, SoftwareFJError

logging.basicConfig(
    filename='software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def simular_10_operaciones():
    sala_v = SalaReunion("Sala de Juntas VIP", 80)
    pc_gamer = AlquilerEquipo("PC Alta Gama", 40)
    profe_py = AsesoriaEspecializada("Asesoría Python", 120)

    escenarios = [
        (1, "Vanessa Jimenez", "vanessa@mail.com", sala_v, 3, {"descuento": 15}),
        (2, "Juan Perez", "juan@mail.com", pc_gamer, 2, {"tiene_seguro": True}),
        (3, "X", "error@com", profe_py, 10, {}),
        (4, "Carlos Ruiz", "carlos@mail", sala_v, -5, {}),
        (5, "Ana Lopez", "ana@u.com", profe_py, 6, {}),
        (6, "Pedro", "pedro@noemail", pc_gamer, 1, {"tiene_seguro": False}),
        (7, "Luis Diaz", "luis@mail.com", sala_v, 2, {"descuento": 10}),
        (8, "Marta Sanchez", "marta@mail.com", pc_gamer, 5, {}),
        (9, "Raul Gomez", "raul@mail.com", sala_v, 0, {}),
        (10, "Sofia Rojas", "sofia@mail.com", profe_py, 2, {}),
    ]

    for i, datos in enumerate(escenarios, 1):
        print(f"--- OPERACIÓN #{i} ---")
        try:
            cliente_temp = Cliente(datos[0], datos[1], datos[2])
            reserva_temp = Reserva(cliente_temp, datos[3], datos[4])
            pago = reserva_temp.procesar(**datos[5])
            print(f"SISTEMA: Pago procesado: ${pago}")
        except (ValidacionDatosError, ReservaInvalidaError) as e:
            print(f"AVISO: {e}")
        except Exception as e:
            print(f"CRÍTICO: {e}")

if __name__ == "__main__":
    simular_10_operaciones()