from datetime import datetime

def calcular_edad(fecha_nacimiento_str):
    """Calcula la edad a partir de una fecha en formato 'YYYY-MM-DD'."""
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
    hoy = datetime.today().date()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def fecha_actual_str():
    """Devuelve la fecha actual en formato 'YYYY-MM-DD'."""
    return datetime.today().strftime("%Y-%m-%d")