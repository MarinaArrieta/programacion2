from utils.file_manager import cargar_datos, guardar_datos

DATA_FILE = 'historias_clinicas.json'

def agregar_historia(documento_paciente, fecha, enfermedad, medico, observaciones):
    historias = cargar_datos(DATA_FILE)

    nueva_historia = {
        "documento_paciente": documento_paciente,
        "fecha": fecha,
        "enfermedad": enfermedad,
        "medico": medico,
        "observaciones": observaciones
    }

    historias.append(nueva_historia)
    guardar_datos(DATA_FILE, historias)
    print(f"Historia clínica agregada para paciente {documento_paciente}.")
    return nueva_historia