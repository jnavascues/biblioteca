import re


class validacion:
    def __init__(self, ):
        pass
    

    def validar_titulo(self, titulo):
        patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        validacion = re.match(patron, titulo)
        return validacion

    def validar_autor(self, autor):
        patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        validacion = re.match(patron, autor)
        return validacion

    def validar_genero(self, genero):
        patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        validacion = re.match(patron, genero)
        return validacion



if __name__ == '__main__':
    validador = validacion()
    if validador.validar_titulo('pasajero'):
        print("bien hecho") 
    else:
        print("Error","Se debe iniciar y terminar con letra o palabra. \
              \n Las letras o palabras se pueden separar por un espacio, \
              un - o un _.  ") 
