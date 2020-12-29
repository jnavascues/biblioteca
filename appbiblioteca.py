from tkinter import Label, Button, Entry, Tk, Grid, Pack, mainloop, W, S, E, N, Scrollbar
import tkinter.ttk as ttk
from tkinter.messagebox import showerror

from base import Abmc
from validador import Validacion


class AppBiblioteca():
    """
    Clase controladora que se encarga de graficar con Tkinter la app
    """

    def __init__(self,):
        # Iniciando Base de datos
        self.base_de_datos = Abmc()
        # Iniciando validador
        self.obj_validar = Validacion()
        # Iniciando Tkinter y graficando
        self.root = Tk()
        self.root.title('Biblioteca')
        self.root.geometry("776x300")
        Label(self.root, text="Biblioteca", bg='green', foreground='white').grid(
            row=0,
            sticky=W+S+N+E,
            columnspan=10
        )
        self.root.grid_columnconfigure(0, pad=50)
        self.agregar_label("Titulo", 1, 0)
        self.agregar_label("Autor", 3, 0)
        self.agregar_label("Genero", 5, 0)
        self.ctitulo = self.agregar_input('', 30, 2, 0)
        self.cautor = self.agregar_input('', 30, 4, 0)
        self.cgenero = self.agregar_input('', 30, 6, 0)
        self.balta = self.agregar_boton(8, 0, 'Alta', self.dar_alta)
        self.bbaja = self.agregar_boton(8, 1, 'Baja', self.dar_baja)
        self.bmodificar = self.agregar_boton(9, 0,
                                             'Modificar', self.dar_modificar)
        self.blimpiar = self.agregar_boton(9, 1, 'Limpiar', self.limpiar)
        self.agregar_treeview(self.root)
        mainloop()

    def refrescar_lista(self,):
        """
        Metodo para recargar los libros de la base de datos en treeview
        """
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)
        biblioteca = self.base_de_datos.cargarlista()
        if biblioteca == 'ERROR':
            showerror("Error en listado", "Error. \
                    \nSe registro un error al cargar los libros \
                    \nPor favor verificar logs de consola.")
            return
        for libro in biblioteca:
            self.my_tree.insert(
                parent='',
                index='end',
                iid=libro[0],
                text=" ",
                values=(libro[0], libro[1], libro[2], libro[3])
            )

    def dar_alta(self,):
        """
        Metodo para el boton de alta de tkinter
        """
        if not self.verificador():
            return
        resultado = self.base_de_datos.alta(
            self.ctitulo.get(), self.cautor.get(), self.cgenero.get())
        if resultado == 'ERROR':
            showerror("Error en Alta", "Error. \
                    \nSe registro un error al dar el alta. \
                    \nPor favor verificar logs de consola.")
        self.refrescar_lista()
        self.limpiar()

    def limpiar(self,):
        """
        Metodo de limpieza de Campos en el formulario
        """
        self.ctitulo.delete(0, 'end')
        self.cautor.delete(0, 'end')
        self.cgenero.delete(0, 'end')

    def dar_baja(self,):
        """
        Metodo del boton tkinter para Bajas
        """
        item = self.my_tree.focus()
        resultado = self.base_de_datos.baja(item)
        if resultado == 'ERROR':
            showerror("Error en Baja", "Error. \
                    \nSe registro un error al dar la baja del libro \
                    \nPor favor verificar logs de consola.")
        self.refrescar_lista()
        self.limpiar()

    def dar_modificar(self,):
        """
        Metodo del boton tkinter para Modificar libros
        """
        if not self.verificador():
            return
        item = self.my_tree.focus()
        datos = self.my_tree.item(item)
        resultado = self.base_de_datos.modificar(
            datos['values'][0], self.ctitulo.get(), self.cautor.get(), self.cgenero.get())
        if resultado == 'ERROR':
            showerror("Error al Modificar", "Error. \
                    \nSe registro un error al modificar el libro \
                    \nPor favor verificar logs de consola.")
        self.refrescar_lista()
        self.limpiar()

    def verificador(self,):
        """
        Metodo Para verificar los campos usando la clase Validacion
        """
        if not self.obj_validar.validar_titulo(self.ctitulo.get()):
            showerror("Error Titulo", "Error en la validacion. \
                    \nEn el campo titulo estan permitidos letras, numeros, \
                    espacios, dos puntos y guiones medios y bajos.\
                    \nNo se permiten otros caracteres especiales. ")
            return False
        if not self.obj_validar.validar_autor(self.cautor.get()):
            showerror("Error Autor", "Error en la validacion. \
                    \nEn el campo Autor se permiten letras y espacios. \
                    \nNo se permiten caracteres especiales.")
            return False
        if not self.obj_validar.validar_genero(self.cgenero.get()):
            showerror("Error Genero", "Error en la validacion. \
                    \nEn el campo Genero se permiten letras y espacios. \
                    \nNo se permiten caracteres especiales.")
            return False
        return True

    def agregar_input(self,
                      valor,
                      ancho,
                      fila,
                      columna):
        """
        Metodo para agregar Inputs en el formulario.
        Argumentos:
        valor: Texto por defecto del campo entry. Puede ser nulo.
        ancho: tamaño en pixeles del campo entry.
        fila: ubicación del campo en la grilla.
        columna: ubicación del campo en la grilla.
        """
        self.objentry = Entry(
            self.root,
            width=ancho
        )
        self.objentry.grid(
            row=fila,
            column=columna,
            columnspan=2
        )
        self.objentry.insert(0, valor)
        return self.objentry

    def agregar_label(self,
                      valor,
                      fila,
                      columna):
        """
        Metodo para agregar Labels en el formulario.
        Argumentos:
        valor: Texto para el label.
        fila: ubicación del label en la grilla.
        columna: ubicación del label en la grilla.
        """
        Label(self.root, text=valor).grid(
            row=fila,
            column=columna,
            sticky=W,
            padx=50,
            columnspan=2
        )

    def agregar_boton(self,
                      row,
                      column,
                      text,
                      comando):
        """
        Metodo para agregar Botones en el formulario con Funciones dinamicas
        Argumentos:
        row: ubicación del botón en la grilla.
        column: ubicación del botón en la grilla.
        text: Texto por defecto del boton.
        comando: Función ligada al botón
        """
        self.objbutton = Button(
            self.root,
            text=text,
            padx=5,
            width=12,
            command=comando
        )
        self.objbutton.grid(
            row=row,
            column=column
        )
        return self.objbutton

    def agregar_treeview(self,
                         parent):
        """
        Metodo para agregar Treeview y cargarlo con sqlite
        Argumento:
        Parent: Objeto de TK
        """
        self.my_tree = ttk.Treeview(parent, selectmode='browse')
        self.my_tree.grid(
            row=1,
            column=4,
            rowspan=10,
            pady=20,
            padx=20
        )
        vsb = Scrollbar(parent, orient="vertical", command=self.my_tree.yview)
        vsb.place(relx=0.978, rely=0.150, relheight=0.650, relwidth=0.020)
        self.my_tree.configure(yscrollcommand=vsb.set)
        self.my_tree['columns'] = (
            'ID',
            'Titulo',
            'Autor',
            'Genero'
        )
        # CreandoColumnas
        self.my_tree.column(
            '#0',
            width=0,
            minwidth=1
        )
        self.my_tree.column(
            'ID',
            anchor=W,
            width=20
        )
        self.my_tree.column(
            'Titulo',
            anchor=W,
            width=200
        )
        self.my_tree.column(
            'Autor',
            anchor=W,
            width=120
        )
        self.my_tree.column(
            'Genero',
            anchor=W,
            width=120
        )
        # Creado Headings
        self.my_tree.heading(
            '#0',
            text=' ',
            anchor=W
        )
        self.my_tree.heading(
            'ID',
            text='ID',
            anchor=W
        )
        self.my_tree.heading(
            'Titulo',
            text='Tirulo',
            anchor=W
        )
        self.my_tree.heading(
            'Autor',
            text='Autor',
            anchor=W
        )
        self.my_tree.heading(
            'Genero',
            text='Genero',
            anchor=W
        )
        self.my_tree.bind(
            '<ButtonRelease-1>',
            self.cargar_item
        )
        self.refrescar_lista()
        self.my_tree.pack

    def cargar_item(self,
                    *args):
        """
        Metodo para cargar la seleccion de un Item en Treeview en el formulario 
        """
        item = self.my_tree.focus()
        datos = self.my_tree.item(item)
        self.ctitulo.delete(0, 'end')
        self.ctitulo.insert(0, datos['values'][1])
        self.cautor.delete(0, 'end')
        self.cautor.insert(0, datos['values'][2])
        self.cgenero.delete(0, 'end')
        self.cgenero.insert(0, datos['values'][3])
