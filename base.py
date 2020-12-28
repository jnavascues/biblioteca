import sqlite3
import re
from validador import validacion


class abmc:
    """
    Clase encargada del Manejo de ABMC con SQLITE3
    """
    def __init__(self, 
            ):
       self.obj_validar = validacion()

    def creardb(self, 
            ):
        """
        Metodo para crear la base de datos y la tabla
        """
        self.conexion=sqlite3.connect("biblioteca.db")
        try:
            self.conexion.execute("""create table libros (
                                    id integer primary key autoincrement,
                                    titulo text,
                                    autor text,
                                    genero text
                                    )""")
            print("se creo la tabla articulos")                        
        except sqlite3.OperationalError:
            print("La tabla libros ya existe")                    
        self.conexion.close()

    def alta(
            self,
            titulo,
            autor,
            genero):
        """
        Metodo para Altas de nuevos libros con validaciones
        """
        self.conexion = sqlite3.connect("biblioteca.db")
        print(titulo)
        if not self.obj_validar.validar_titulo(titulo):
           return "Titulo no valido"          
        if not self.obj_validar.validar_autor(autor):
            return "Autor no valido"  
        if not self.obj_validar.validar_genero(genero):
            return "genero no valido"            
        self.conexion.execute("insert into libros(titulo,autor,genero) \
                        values (?,?,?)", [titulo, autor, genero])
        self.conexion.commit()
        self.conexion.close()

    def cargarlista(self, 
            ):
        """
        Metodo traer la tabla libros completa a una lista
        """
        self.conexion = sqlite3.connect('biblioteca.db')
        biblioteca = self.conexion.execute('SELECT * FROM libros')
        return biblioteca

    def baja(self, 
            id):
        """
        Metodo para la baja de un libro
        """
        self.conexion = sqlite3.connect('biblioteca.db')
        self.conexion.execute('DELETE FROM libros WHERE id = ?', [id])
        self.conexion.commit()
        self.conexion.close()

    def modificar(self,
            ide, 
            titulo, 
            autor, 
            genero):
        """
        Metodo para modificar un libro existente
        """
        self.conexion = sqlite3.connect('biblioteca.db')
        self.conexion.execute('UPDATE libros SET titulo = ?, autor = ? , genero = ? \
                        WHERE id = ?', [titulo, autor, genero, ide])
        self.conexion.commit()
        self.conexion.close()

"""
    def validartitulo(
            titulo):
        patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        validacion = re.match(patron, titulo)
        return validacion

"""