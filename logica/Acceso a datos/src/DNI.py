from DNI import DNI
import pytest

class DNI:
    @staticmethod
    def __init__(self,dni):
        self.__dni = dni

    letras_dni = list('T R W A G Y F P D X B N J Z S Q V H L C K E'.replace('\t','').replace(' ', ''))

    DNI = input('Inserta tu DNI: ')
    DNI_numero = int(DNI[0:-1])
    dni_letra = DNI[-1]

        letra_posicion = DNI_numero % len(letras_dni)

        if dni_letra == letras_dni[letra_posicion]:
            print('Su dni es correcto')
        else:
            print('DNI incorrecto')