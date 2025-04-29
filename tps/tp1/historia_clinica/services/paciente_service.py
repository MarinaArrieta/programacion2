import json
import os

DATA_FILE = 'data/pacientes.json'

def cargar_pacientes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_pacientes(pacientes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, indent=2, ensure_ascii=False)

def registrar_paciente(documento, apellido, nombre, fecha_nacimiento, nacionalidad):
    pacientes = cargar_pacientes()

    nuevo_paciente = {
        "numero_historia": len(pacientes) + 1,
        "documento": documento,
        "apellido": apellido,
        "nombre": nombre,
        "fecha_nacimiento": fecha_nacimiento,
        "nacionalidad": nacionalidad
    }

    pacientes.append(nuevo_paciente)
    guardar_pacientes(pacientes)
    print(f"Paciente {nombre} {apellido} registrado exitosamente.")
    return nuevo_paciente

def eliminar_paciente(documento):
    # Cargar los pacientes desde el archivo JSON
    pacientes = cargar_pacientes()

    # Buscar el paciente por documento
    paciente_a_eliminar = None
    for paciente in pacientes:
        if paciente['documento'] == documento:
            paciente_a_eliminar = paciente
            break

    if paciente_a_eliminar:
        # Eliminar el paciente de la lista
        pacientes.remove(paciente_a_eliminar)
        # Guardar la lista actualizada en el archivo
        guardar_pacientes(pacientes)
        print(f"Paciente con documento {documento} eliminado exitosamente.")
    else:
        print(f"No se encontró un paciente con documento {documento}.")