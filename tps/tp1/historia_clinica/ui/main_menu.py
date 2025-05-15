from ui.paciente_menu import menu_pacientes
from ui.medico_menu import menu_medicos
from ui.historia_menu import menu_historias

def ejecutar_menu_principal():
    while True:
        print("\n=== Sistema de Historia Clínica ===")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Historias Clínicas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_historias()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")