class Paciente:
    def __init__(self, documento, apellido, nombre, fecha_nacimiento, numero_historia, nacionalidad):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento  # Formato: 'YYYY-MM-DD'
        self.numero_historia = numero_historia
        self.nacionalidad = nacionalidad
        self.historias_clinicas = []  # Lista de instancias de HistoriaClinica

    def calcular_edad(self, fecha_actual):
        from datetime import datetime
        nacimiento = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.strptime(fecha_actual, "%Y-%m-%d")
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad
