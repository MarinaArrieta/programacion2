from services.paciente_service import registrar_paciente, eliminar_paciente
# , editar_paciente, buscar_paciente

def menu_paciente():
    while True:
        print("\n--- Menú de Pacientes ---")
        print("1. Registrar nuevo paciente")
        print("2. Editar paciente existente")
        print("3. Eliminar paciente")
        print("4. Buscar paciente")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            doc = input("Documento: ")
            ape = input("Apellido: ")
            nom = input("Nombre: ")
            fnac = input("Fecha de nacimiento (YYYY-MM-DD): ")
            nac = input("Nacionalidad: ")
            registrar_paciente(doc, ape, nom, fnac, nac)

        # elif opcion == '2':
        #     doc = input("Documento del paciente a editar: ")
        #     print("Deje en blanco para no modificar un campo")
        #     ape = input("Nuevo apellido: ") or None
        #     nom = input("Nuevo nombre: ") or None
        #     fnac = input("Nueva fecha de nacimiento (YYYY-MM-DD): ") or None
        #     nac = input("Nueva nacionalidad: ") or None
        #     editar_paciente(doc, ape, nom, fnac, nac)

        elif opcion == '3':
            doc = input("Documento del paciente a eliminar: ")
            eliminar_paciente(doc)

        # elif opcion == '4':
        #     print("\nBuscar por:")
        #     print("1. Apellido y/o Nombre")
        #     print("2. Rango de fechas de atención")
        #     print("3. Enfermedad/afección")
        #     print("4. Médico tratante")
        #     print("5. Nacionalidad")
        #     tipo = input("Opción de búsqueda: ")
        #     buscar_paciente(tipo)

        elif opcion == '5':
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_paciente()
