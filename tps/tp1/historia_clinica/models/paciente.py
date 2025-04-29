class Paciente:
    def __init__(
            self, 
            documento, 
            apellido, 
            nombre, 
            fecha_nacimiento, 
            numero_historia,
            nacionalidad
        ):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.numero_historia = numero_historia
