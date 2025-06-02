
from services.historia_service import agregar_historia_clinica

def menu_historia():
    while True:
        print("\n--- Menú de Historias Clínicas ---")
        print("1. Agregar historia clínica a un paciente")
        print("2. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            documento = input("Documento del paciente: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            enfermedad = input("Enfermedad/Afección: ")
            medico = input("Nombre del médico que lo trató: ")
            observaciones = input("Observaciones: ")
            agregar_historia_clinica(documento, fecha, enfermedad, medico, observaciones)
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
