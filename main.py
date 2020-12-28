from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import *

from bd import *


def refrescar_lista():
    for i in my_tree.get_children(): 
        my_tree.delete(i) 
    biblioteca = cargarlista()  
    for libro in biblioteca:
        my_tree.insert(
            parent='', 
            index='end', 
            iid=libro[0], 
            text=" ", 
            values=(libro[0], libro[1], libro[2], libro[3]))


def dar_alta():
    if validartitulo(ctitulo.get()):   
        alta(ctitulo.get(),cautor.get(),cgenero.get())
        refrescar_lista()
        limpiar()
    else:
        showerror("Error","Se debe iniciar y terminar con letra o palabra. \
                  \nLas letras o palabras se pueden separar por un espacio, \
                  un - o un _.  ") 


def limpiar():
    ctitulo.delete(
        0, 
        'end')
    cautor.delete(
        0, 
        'end')
    cgenero.delete(
        0, 
        'end')


def dar_baja():
    item = my_tree.focus()
    baja(item)
    refrescar_lista()
    limpiar()


def dar_modificar():
    item = my_tree.focus()
    datos = my_tree.item(item)
    modificar(datos['values'][0],ctitulo.get(),cautor.get(),cgenero.get())
    refrescar_lista()
    limpiar()
  

def agregar_input(
        valor,
        ancho,
        fila,
        columna):
    objentry = Entry(
        root, 
        width=ancho)
    objentry.grid(
        row=fila, 
        column=columna, 
        columnspan=2) 
    objentry.insert(0,valor)
    return objentry


def agregar_label(
        valor,
        fila,
        columna):
    objlabel = Label(root, text=valor).grid(
        row=fila, 
        column=columna,
        sticky=W,
        padx=50,
        columnspan=2)
    return objlabel


def cargar_item(
        *args):
    item = my_tree.focus()
    datos = my_tree.item(item)
    ctitulo.delete(0, 'end')
    ctitulo.insert(0,datos['values'][1])
    cautor.delete(0, 'end')
    cautor.insert(0,datos['values'][2])
    cgenero.delete(0, 'end')
    cgenero.insert(0,datos['values'][3])


creardb()

root = Tk()
root.title('Biblioteca')
root.geometry("776x300")

Label(root, text="Biblioteca", bg='green', foreground='white').grid(
    row=0, 
    sticky=W+S+N+E, 
    columnspan=10
    )
root.grid_columnconfigure(0, pad = 50)
agregar_label("Titulo", 1, 0)
agregar_label("Autor", 3, 0)
agregar_label("Genero", 5, 0)
ctitulo = agregar_input('', 30, 2, 0)
cautor = agregar_input('', 30, 4, 0)
cgenero = agregar_input('', 30, 6, 0)


balta = Button(
    root, 
    text="Alta", 
    padx=5, 
    width=12, 
    command=dar_alta
    )
bbaja = Button(
    root, 
    text="Baja", 
    padx=5, 
    width=12, 
    command=dar_baja
    ) 
bmodificar = Button(
    root, 
    text="Modificar", 
    padx=5, 
    width=12, 
    command=dar_modificar
    ) 
blimpiar = Button(
    root, 
    text="Limpiar", 
    padx=5, 
    width=12, 
    command=limpiar
    ) 

balta.grid(
    row=8, 
    column=0
    )
bbaja.grid(
    row=8, 
    column=1
    )
bmodificar.grid(
    row=9, 
    column=0
    )
blimpiar.grid(
    row=9, 
    column=1
    )

my_tree = ttk.Treeview(root)
my_tree.grid(
    row=1, 
    column=4, 
    rowspan=10, 
    pady=20, 
    padx=20
    )
my_tree['columns'] = (
    'ID', 
    'Titulo', 
    'Autor', 
    'Genero'
    )

#CreateColumns
my_tree.column(
    '#0', 
    width=0, 
    minwidth=25
    )
my_tree.column(
    'ID', 
    anchor=W, 
    width=120
    )
my_tree.column(
    'Titulo', 
    anchor=W, 
    width=120
    )
my_tree.column(
    'Autor', 
    anchor=W, 
    width=120
    )
my_tree.column(
    'Genero', 
    anchor=W, 
    width=120
    )

#CreateHeading
my_tree.heading(
    '#0', 
    text=' ', 
    anchor=W
    )
my_tree.heading(
    'ID', 
    text='ID', 
    anchor=W
    )
my_tree.heading(
    'Titulo', 
    text='Tirulo', 
    anchor=W
    )
my_tree.heading(
    'Autor', 
    text='Autor', 
    anchor=W
    )
my_tree.heading(
    'Genero', 
    text='Genero', 
    anchor=W
    )

my_tree.bind(
    '<ButtonRelease-1>', 
    cargar_item
    )

refrescar_lista()

my_tree.pack
mainloop()


