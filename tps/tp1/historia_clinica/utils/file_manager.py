import json
import os

def cargar_datos(nombre_archivo):
    ruta = f"data/{nombre_archivo}"
    if not os.path.exists(ruta):
        return []
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(nombre_archivo, datos):
    ruta = f"data/{nombre_archivo}"
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)