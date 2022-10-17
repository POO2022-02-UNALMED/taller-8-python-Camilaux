from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, años):
        super().__init__(nombre,edad,altura,sexo)
        self._deporte = deporte
        self._añosPracticando = años

    def setDeporte(self,deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self,años):
        self._añosPracticando = años

    def getAñosPracticando(self):
        return self._añosPracticando
