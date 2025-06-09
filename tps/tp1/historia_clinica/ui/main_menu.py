import os
from ui.paciente_menu import menu_paciente
from ui.medico_menu import menu_medico
from ui.historia_menu import menu_historia

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        limpiar_pantalla()
        print("\n=== INSTITUTO MÉDICO LAS LUCIÉRNAGAS ===")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Médicos")
        print("3. Gestión de Historias Clínicas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_paciente()
        elif opcion == '2':
            menu_medico()
        elif opcion == '3':
            menu_historia()
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Presione Enter para continuar...")
            input()

if __name__ == '__main__':
    main_menu()
