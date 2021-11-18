# This is a sample Python script.

from Matriz import Matriz
from Mensaje import Mensaje
from tkinter import Tk, Label, Button
from tkinter import filedialog
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter import scrolledtext
import tkinter as tk
from Interfaz import Interfaz


def abrir_archivo():

    archivo_abierto = askopenfile(mode='r', filetypes=[('Archivos de texto', '*.txt')])
    area_p_escribir = scrolledtext.ScrolledText(width=40, height=30, wrap=tk.WORD)
    area_p_escribir.pack()
    if archivo_abierto is not None:
        contenido = archivo_abierto.read()
        d = Matriz()
        m = Mensaje(contenido)
        mensaje = m.seccionar(m.codifica())
        codi = d.mensajecodificado(mensaje)
        men_desec = m.deseccionar(codi)
        res = [str(i) for i in men_desec]
        enviar = " ".join(res)
        #archivo_abierto.write(enviar)
        # deco = m.decodifica(men_desec)
        # area_p_escribir.insert(tk.INSERT, deco)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ventana = Tk()
    interfaz = Interfaz(ventana)
    interfaz.inicia()


    #d = Matriz()
    #d.mostrarma()

    #d.obtdetmatriz()
    #print(d.obtdetmatriz())
    #print(d.adjtrans())
    #print(d.inversa())
    # m= Mensaje("MEET ME MONDAY")
    # mensaje=m.seccionar(m.codifica())
    # print(mensaje)
    # print(mensaje[0:1])
    # var=mensaje[0:1]
    # #print(var[1][2])
    # print(d.multiplica(var))
    # codi = d.mensajecodificado(mensaje)
    # print(codi)
    # decodi = d.mensajedecodificado(codi)
    # print(decodi)
    # men_desec = m.deseccionar(decodi)
    # print(men_desec)
    # deco = m.decodifica(men_desec)
    # print(deco)


    # entry = ttk.Entry(ventana)
    # Posicionarla en la ventana.
    # entry.place(x=50, y=50)
    #d.multiplica(var)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
