from sys import exc_info as exc_info
import sqlite3


class Abmc:
    """
    Clase encargada del Manejo de ABMC con SQLITE3
    """

    def __init__(self,
                 ):
        self.conexion = self.conectar()
        self.creardb()

    def conectar(self,):
        """
        Metodo para la conexion a la base SQLITE3
        """
        conexion = sqlite3.connect("biblioteca.db")
        return conexion

    def creardb(self,
                ):
        """
        Metodo para crear la base de datos y la tabla
        """
        try:
            self.conexion.execute("""create table libros (
                                    id integer primary key autoincrement,
                                    titulo text,
                                    autor text,
                                    genero text
                                    )""")
            print("Consola: Se creo la tabla articulos")
        except sqlite3.OperationalError:
            print("Consola: La tabla libros ya existe. Detalle: ",
                  exc_info()[1])
        except:
            print("Consola: Error en la creacion de la tabla. ",
                  exc_info()[0], exc_info()[1])

    def alta(
            self,
            titulo,
            autor,
            genero):
        """
        Metodo para Altas de nuevos libros con validaciones
        Argumentos:
        titulo: se espera el nombre del libro a ingresar.
        autor: se espera el autor del libro a ingresar.
        genero: se espera el genero del libro a ingresar.
        
        """
        try:
            self.conexion.execute("insert into libros(titulo,autor,genero) \
                            values (?,?,?)", [titulo, autor, genero])
            self.conexion.commit()
        except:
            print("Consola: Error al alta de un nuevo Libro. ",
                  exc_info()[0], exc_info()[1])
            return "ERROR"

    def cargarlista(self,
                    ):
        """
        Metodo traer la tabla libros completa a una lista.
        Si falla la carga se retorna ERROR
        """
        try:
            biblioteca = self.conexion.execute('SELECT * FROM libros')
        except:
            print("Consola: Error al abrir la Tabla Libros. ",
                  exc_info()[0], exc_info()[1])
            return "ERROR"
        return biblioteca

    def baja(self,
             id):
        """
        Metodo para la baja de un libro
        """
        try:
            self.conexion.execute('DELETE FROM libros WHERE id = ?', [id])
            self.conexion.commit()
        except:
            print("Consola: Error al borrar un libro. ",
                  exc_info()[0], exc_info()[1])
            return "ERROR"
        return "OK"

    def modificar(self,
                  ide,
                  titulo,
                  autor,
                  genero):
        """
        Metodo para modificar un libro existente
        Argumentos:
        titulo: se espera el nombre del libro a ingresar.
        autor: se espera el autor del libro a ingresar.
        genero: se espera el genero del libro a ingresar.

        """
        try:
            self.conexion.execute('UPDATE libros SET titulo = ?, autor = ? , genero = ? \
                            WHERE id = ?', [titulo, autor, genero, ide])
            self.conexion.commit()
        except:
            print("Consola: Error al modificar un registro. ",
                  exc_info()[0], exc_info()[1])
            return "ERROR"
        return "OK"
