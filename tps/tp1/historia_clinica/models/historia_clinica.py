class HistoriaClinica:
    def __init__(self, fecha, afeccion, medico, observaciones):
        self.fecha = fecha  # Formato: 'YYYY-MM-DD'
        self.afeccion = afeccion
        self.medico = medico  # Instancia de Medico
        self.observaciones = observaciones
