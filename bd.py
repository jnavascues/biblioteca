import sqlite3

#Funcion que crea el backend, DB  y table
def creardb():
        conexion=sqlite3.connect("biblioteca.db")
        try:
            conexion.execute("""create table libros (
                                    id integer primary key autoincrement,
                                    titulo text,
                                    autor text,
                                    genero text
                                )""")
            print("se creo la tabla articulos")                        
        except sqlite3.OperationalError:
            print("La tabla libros ya existe")                    
        conexion.close()

def alta(titulo,autor,genero):
    conexion = sqlite3.connect("biblioteca.db")
    print(titulo)
    conexion.execute("insert into libros(titulo,autor,genero) values (?,?,?)", [titulo, autor, genero])
    conexion.commit()
    conexion.close()


def cargarlista():
    conexion = sqlite3.connect('biblioteca.db')
    biblioteca = conexion.execute('SELECT * FROM libros')
    return biblioteca

def baja(id):
    conexion = sqlite3.connect('biblioteca.db')
    conexion.execute('DELETE FROM libros WHERE id = ?', [id])
    conexion.commit()
    conexion.close()


def modificar(ide, titulo, autor, genero):
    conexion = sqlite3.connect('biblioteca.db')
    sentencia = "UPDATE libros SET titulo = '" + str(titulo) + "' , autor = '" + str(autor) + "' , genero = '" + str(genero) + "' WHERE id = '" + str(ide) + "'"
    print(sentencia)
    conexion.execute(sentencia)
    #conexion.execute('UPDATE libros SET titulo = ?, autor = ? , genero = ? WHERE id = ?', [titulo, autor, genero, ide])
    conexion.commit()
    conexion.close()