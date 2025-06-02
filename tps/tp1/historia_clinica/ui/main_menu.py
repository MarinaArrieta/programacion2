import os
from ui.paciente_menu import mostrar_menu_pacientes
from ui.medico_menu import mostrar_menu_medicos
from ui.historia_menu import mostrar_menu_historias

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
            mostrar_menu_pacientes()
        elif opcion == '2':
            mostrar_menu_medicos()
        elif opcion == '3':
            mostrar_menu_historias()
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Presione Enter para continuar...")
            input()

if __name__ == '__main__':
    main_menu()
