import json
import os

DATA_FILE = 'data/historias_clinicas.json'

def cargar_historias():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_historias(historias):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(historias, f, indent=2, ensure_ascii=False)

def registrar_historia(fecha_ingreso, fecha_egreso, afeccion, medico, observaciones):
    historias = cargar_historias()

    nuevo_historia = {
        "fecha_ingreso": fecha_ingreso,
        "fecha_egreso": fecha_egreso,
        "afeccion": afeccion,
        "medico": medico,
        "observaciones": observaciones,
    }

    historias.append(nuevo_historia)
    guardar_historias(historias)
    print(f"Historia, Medico: {medico} - afeccion: {afeccion} registrado exitosamente.")
    return nuevo_historia
