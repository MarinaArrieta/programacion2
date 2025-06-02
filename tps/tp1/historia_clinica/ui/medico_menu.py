
from services.medico_service import (
    registrar_medico,
    listar_medicos
)

def menu_medico():
    while True:
        print("\n--- Menú de Médicos ---")
        print("1. Registrar nuevo médico")
        print("2. Listar médicos")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            registrar_medico(apellido, nombre, especialidad)
        elif opcion == "2":
            listar_medicos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
