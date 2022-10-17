from persona import Persona
from deportista import Deportista

class Futbolista(Deportista):

    _listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años, goles, tarjetas, pierna):
        super().__init__(nombre,edad,altura,sexo,"Futbol", años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        Futbolista._listaFutbolistas.append(self)

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles

    def getGolesMarcados(self):
        return self._golesMarcados

    def setTarjetasRojas(self, tarjeta):
        self._tarjetasRojas = tarjeta
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna

    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def setListaFutbolistas(cls,lista):
        cls._listaFutbolistas = lista

    @classmethod
    def setListaFutbolistas(cls):
        return cls._listaFutbolistas

    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
