from tkinter import *
import os
from tkinter.ttk import *
ventana = Tk()
ventana.title("Cuentas y contraseñas")
#img = PhotoImage(file='candado.ico')
#ventana.tk.call('wm', 'iconphoto', ventana._w, img)
#ventana.iconbitmap("candado.ico")

#ZONA DE FUNCIONES
arreglo = []
def guardar():
    arreglo.append(Nombre.get())
    arreglo.append(Pagina.get())
    arreglo.append(Correo.get())
    arreglo.append(Contraseña.get())
    
def mostrar():
    textoGigante.delete(index1=0)
    textoGigante.insert(INSERT,arreglo)
#ZONA DE LABELS

labelNombre = Label(ventana,text= "Nombre--")
labelNombre.grid(row=1, column=1)

labelPagina = Label(ventana,text= "--Pagina--")
labelPagina.grid(row=1, column=2)

labelCorreo = Label(ventana,text= "--Correo--")
labelCorreo.grid(row=1, column=3)

labelContraseña = Label(ventana,text= "--Contraseña")
labelContraseña.grid(row=1, column=4)

#ZONA DE ENTRYS
Nombre = StringVar()
Pagina = StringVar()
Correo = StringVar()
Contraseña = StringVar()
entryNombre = Entry(ventana, textvariable=Nombre)
entryNombre.grid(row=2, column = 1)

entryPagina = Entry(ventana, textvariable=Pagina)
entryPagina.grid(row=2, column = 2)

entryCorreo = Entry(ventana, textvariable=Correo)
entryCorreo.grid(row=2, column = 3)

entryContraseña = Entry(ventana, textvariable=Contraseña)
entryContraseña.grid(row=2, column = 4)

#ZONA DE BOTONES

botonAceptar = Button(ventana, text="Aceptar", command=lambda:guardar())
botonAceptar.grid(row=3, column=1, columnspan=5)

botonAceptar = Button(ventana, text="Mostrar", command=lambda:mostrar())
botonAceptar.grid(row=5, column=1, columnspan=5)


"""
for c in range(5):
    if c==0:
        pass
    else:
"""

textoGigante = Text(ventana)
textoGigante.grid(row=4, column=1, columnspan=5)


#MAINLOOP

ventana.mainloop()

