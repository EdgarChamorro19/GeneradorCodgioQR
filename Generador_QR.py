from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
ventana=Tk()
ventana.title("Generador QR")

def Generar():
    if len(subject.get())!= 0:
        global miQR
        miQR=pyqrcode.create(subject.get())
        ImagenQR=miQR.xbm(scale=6)
        global foto
        foto=BitmapImage(data=ImagenQR)
    else:
        messagebox.showinfo("Error")
    try:
        mostrarcodigo()
    except:
        pass

def mostrarcodigo():
    global foto
    notificationlabel.config(image=foto)
    subeti.config(text="Mostrando el codigo QR para: "+subject.get())
    

def guardar():
    dir = path1 = os.getcwd()+"\Codigos QR"
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    try:
        if len(nombre.get()) != 0:
            ImagenQR=miQR.png(os.path.join(dir, nombre.get() + ".png" ),scale=6)
        else:
            messagebox.showinfo("Error")
    except:
        messagebox.showinfo("Error","Por favor Genere el Codigo Qr Primero")

eti1=Label(ventana, text="Ingrese un Nombre",font=("Helvetica",12))
eti1.grid(row=0,column=0,sticky=N + S + E + W)

eti2=Label(ventana, text="Ingrese el nombre del Archivo",font=("Helvetica",12))
eti2.grid(row=1,column=0,sticky=N + S + E + W)

subject=StringVar()
subjectEntrada=Entry(ventana,textvariable=subject,font=("Helvetica",12))
subjectEntrada.grid(row=0,column=1,sticky=N + S + E + W)

nombre=StringVar()
nombreEntrada=Entry(ventana,textvariable=nombre,font=("Helvetica",12))
nombreEntrada.grid(row=1,column=1,sticky=N + S + E + W)

boton=Button(ventana, text="Crear Codigo QR",font=("Helvetica",12),width=15, command=Generar)
boton.grid(row=0,column=3,sticky=N + S + E + W)


notificationlabel=Label(ventana)
notificationlabel.grid(row=2,column=1,sticky=N + S + E + W)

subeti=Label(ventana,text="")
subeti.grid(row=3,column=1,sticky=N + S + E + W)

mostrarBoton=Button(ventana,text="Guardar como PNG",font=("Helvetica",12),width=15, command=guardar)
mostrarBoton.grid(row=1,column=3,sticky=N + S + E + W)

totalRows=3
totalcols=3

for row in range (totalRows +1):
    ventana.grid_rowconfigure(row,weight=1)
for col in range(totalcols + 1):
    ventana.grid_columnconfigure(col,weight=1)




ventana.mainloop()