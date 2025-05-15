from services.paciente_service import registrar_paciente, eliminar_paciente, cargar_pacientes

def menu_pacientes():
    while True:
        print("\n--- Menú de Pacientes ---")
        print("1. Registrar nuevo paciente")
        print("2. Mostrar todos los pacientes")
        print("3. Eliminar paciente")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            documento = input("Documento: ")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            nacionalidad = input("Nacionalidad: ")
            registrar_paciente(documento, apellido, nombre, fecha_nacimiento, nacionalidad)

        elif opcion == "2":
            pacientes = cargar_pacientes()
            print("\n--- Lista de pacientes ---")
            for p in pacientes:
                print(f"{p['numero_historia']}. {p['nombre']} {p['apellido']} - Documento: {p['documento']}")

        elif opcion == "3":
            documento = input("Ingrese el documento del paciente a eliminar: ")
            eliminar_paciente(documento)

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")