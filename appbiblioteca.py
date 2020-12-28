from tkinter import Label,Button,Entry,Tk,Grid,Pack,mainloop,W,S,E,N
import tkinter.ttk as ttk
from tkinter.messagebox import showerror

from bd import baja,alta,modificar,creardb,cargarlista,validartitulo


class AppBiblioteca():
    def __init__(self,):
        creardb()
        self.root = Tk()
        self.root.title('Biblioteca')
        self.root.geometry("776x300")
        Label(self.root, text="Biblioteca", bg='green', foreground='white').grid(
            row=0, 
            sticky=W+S+N+E, 
            columnspan=10
            )
        self.root.grid_columnconfigure(0, pad = 50)
        self.agregar_label("Titulo", 1, 0)
        self.agregar_label("Autor", 3, 0)
        self.agregar_label("Genero", 5, 0)
        self.ctitulo = self.agregar_input('', 30, 2, 0)
        self.cautor = self.agregar_input('', 30, 4, 0)
        self.cgenero = self.agregar_input('', 30, 6, 0)
        self.balta = self.agregar_boton(8,0,'Alta',self.dar_alta)
        self.bbaja = self.agregar_boton(8,1,'Baja',self.dar_baja)
        self.bmodificar = self.agregar_boton(9,0,'Modificar',self.dar_modificar)
        self.blimpiar = self.agregar_boton(9,1,'Limpiar',self.limpiar)
        self.agregar_treeview(self.root)
        mainloop()


    def refrescar_lista(self,):
        for i in self.my_tree.get_children(): 
            self.my_tree.delete(i) 
        biblioteca = cargarlista()  
        for libro in biblioteca:
            self.my_tree.insert(
                parent='', 
                index='end', 
                iid=libro[0], 
                text=" ", 
                values=(libro[0], libro[1], libro[2], libro[3]))


    def dar_alta(self,):
        if validartitulo(self.ctitulo.get()):   
            alta(self.ctitulo.get(),self.cautor.get(),self.cgenero.get())
            self.refrescar_lista()
            self.limpiar()
        else:
            showerror("Error","Se debe iniciar y terminar con letra o palabra. \
                    \nLas letras o palabras se pueden separar por un espacio, \
                    un - o un _.  ") 


    def limpiar(self,):
        self.ctitulo.delete(
            0, 
            'end')
        self.cautor.delete(
            0, 
            'end')
        self.cgenero.delete(
            0, 
            'end')


    def dar_baja(self,):
        item = self.my_tree.focus()
        baja(item)
        self.refrescar_lista()
        self.limpiar()


    def dar_modificar(self,):
        item = self.my_tree.focus()
        datos = self.my_tree.item(item)
        modificar(datos['values'][0],self.ctitulo.get(),self.cautor.get(),self.cgenero.get())
        self.refrescar_lista()
        self.limpiar()
    

    def agregar_input(self,
            valor,
            ancho,
            fila,
            columna):
        self.objentry = Entry(
            self.root, 
            width=ancho)
        self.objentry.grid(
            row=fila, 
            column=columna, 
            columnspan=2) 
        self.objentry.insert(0,valor)
        return self.objentry

    def agregar_label(self,
            valor,
            fila,
            columna):
        Label(self.root, text=valor).grid(
            row=fila, 
            column=columna,
            sticky=W,
            padx=50,
            columnspan=2)

    def agregar_boton(self, 
        row,
        column,
        text,
        comando):
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
        self.my_tree = ttk.Treeview(parent)
        self.my_tree.grid(
            row=1, 
            column=4, 
            rowspan=10, 
            pady=20, 
            padx=20
            )
        self.my_tree['columns'] = (
            'ID', 
            'Titulo', 
            'Autor', 
            'Genero'
            )
        #CreandoColumnas
        self.my_tree.column(
            '#0', 
            width=0, 
            minwidth=25
            )
        self.my_tree.column(
            'ID', 
            anchor=W, 
            width=120
            )
        self.my_tree.column(
            'Titulo', 
            anchor=W, 
            width=120
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
        #Creado Headings
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
        item = self.my_tree.focus()
        datos = self.my_tree.item(item)
        self.ctitulo.delete(0, 'end')
        self.ctitulo.insert(0,datos['values'][1])
        self.cautor.delete(0, 'end')
        self.cautor.insert(0,datos['values'][2])
        self.cgenero.delete(0, 'end')
        self.cgenero.insert(0,datos['values'][3])
