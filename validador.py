import re


class validacion:
    """
    Clase para validaciones de los campos de entrada
    """
    def __init__(self, ):
        pass
    

    def validar_titulo(self, titulo):
        """
        Metodo de validacion de titulo, se permiten letras espacios y numeros. 
        Guiones medios, bajos y dos puntos tambien estan permitidos
        No se permiten otros caracteres especiales 
        """
        patron = re.compile("^[A-Za-z0-9:]+(?:[ _-][A-Za-z0-9:]+)*$")
        validacion = re.match(patron, titulo)
        return validacion

    def validar_autor(self, autor):
        """
        Metodo de validacion de Autor
        Solo se permites letras.
        """
        patron = re.compile("^[A-Za-z]+(?:[ ][A-Za-z]+)*$")
        validacion = re.match(patron, autor)
        return validacion

    def validar_genero(self, genero):
        """
        Metodo de validacion de genero
        Solo se permites letras y espacios en blanco
        """
        patron = re.compile("^[A-Za-z]+(?:[ ][A-Za-z]+)*$")
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
