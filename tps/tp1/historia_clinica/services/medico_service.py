from utils.file_manager import cargar_datos, guardar_datos

DATA_FILE = 'medicos.json'

def registrar_medico(apellido, nombre, especialidad):
    medicos = cargar_datos(DATA_FILE)

    nuevo_medico = {
        "apellido": apellido,
        "nombre": nombre,
        "especialidad": especialidad
    }

    medicos.append(nuevo_medico)
    guardar_datos(DATA_FILE, medicos)
    print(f"Médico {nombre} {apellido} registrado exitosamente.")
    return nuevo_medico

def listar_medicos():
    return cargar_datos(DATA_FILE)