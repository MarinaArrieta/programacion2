from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
