from dni import DNI
import pytest

class DNI:
    @staticmethod
    def __init__(self,dni):
        self.__dni = dni

    letras_dni = list('T R W A G Y F P D X B N J Z S Q V H L C K E'.replace('\t','').replace(' ', ''))

    DNI = input('Inserta tu DNI: ')

    DNI % len(letras_dni)