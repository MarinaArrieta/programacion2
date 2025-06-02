from utils.file_manager import cargar_datos, guardar_datos

DATA_FILE = 'pacientes.json'

def registrar_paciente(documento, apellido, nombre, fecha_nacimiento, nacionalidad):
    pacientes = cargar_datos(DATA_FILE)

    nuevo_paciente = {
        "numero_historia": len(pacientes) + 1,
        "documento": documento,
        "apellido": apellido,
        "nombre": nombre,
        "fecha_nacimiento": fecha_nacimiento,
        "nacionalidad": nacionalidad
    }

    pacientes.append(nuevo_paciente)
    guardar_datos(DATA_FILE, pacientes)
    print(f"Paciente {nombre} {apellido} registrado exitosamente.")
    return nuevo_paciente

def eliminar_paciente(documento):
    pacientes = cargar_datos(DATA_FILE)
    pacientes_filtrados = [p for p in pacientes if p['documento'] != documento]

    if len(pacientes_filtrados) == len(pacientes):
        print(f"No se encontró un paciente con documento {documento}.")
        return False

    guardar_datos(DATA_FILE, pacientes_filtrados)
    print(f"Paciente con documento {documento} eliminado exitosamente.")
    return True