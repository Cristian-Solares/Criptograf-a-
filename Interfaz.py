
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

class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.matriz = ttk.Entry(ventana)
        
    def inicia(self):
        self.ventana.title("Codificador de mensajes")
        self.ventana.geometry('250x200')
        label = Label(self.ventana, text="Ingrese la matriz de 3x3 separada por comas")
        label.place(x=10, y=60)

        self.matriz.place(x=60, y=90)
        Button(text="codificar", command=self.codificar).place(x=30, y=10)
        Button(text="decodificar", command=self.decodificar).place(x=150, y=10)
        self.ventana.mainloop()

    def codificar(self):
        archivo_abierto = askopenfile(mode='r', filetypes=[('Archivos de texto', '*.txt')])
        #area_p_escribir = scrolledtext.ScrolledText(width=40, height=30, wrap=tk.WORD)
        #area_p_escribir.pack()
        if archivo_abierto is not None:
            contenido = archivo_abierto.read()
            con_ma = self.matriz.get()
            d = Matriz(con_ma)
            m = Mensaje(contenido)
            mensaje = m.seccionar(m.codifica())
            codi = d.mensajecodificado(mensaje)
            men_desec = m.deseccionar(codi)
            res = [str(i) for i in men_desec]
            enviar = " ".join(res)
            ar=open("archivo_mensaje.txt","w")
            ar.write(enviar)
            ar.close()
    def decodificar(self):
        archivo_abierto = askopenfile(mode='r', filetypes=[('Archivos de texto', '*.txt')])
        # area_p_escribir = scrolledtext.ScrolledText(width=40, height=30, wrap=tk.WORD)
        # area_p_escribir.pack()
        if archivo_abierto is not None:
            contenido = archivo_abierto.read()
            con_ma = self.matriz.get()
            d = Matriz(con_ma)
            m = Mensaje(contenido)
            lista_mensaje = contenido.split(sep=' ')
            lista_mensaje_int = [float(i) for i in lista_mensaje]
            decodi = d.mensajedecodificado(lista_mensaje_int)
            

            men_desec = m.deseccionar(decodi)
        
            deco = m.decodifica(men_desec)
            
            enviar = " ".join(deco)
            ar = open("mensaje.txt", "w")
            ar.write(enviar)
            ar.close()