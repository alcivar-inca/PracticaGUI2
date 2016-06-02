from tkinter import *
app = Tk()
app.geometry('600x400+350+70')

def mostrarArchivo():
	archivo = open('texto1.txt', 'r')
	linea=archivo.read()
	archivo.close()
	mensaje = Message(app, text=linea)
	mensaje.config(bg = 'lightgreen', font=('arial', 30, 'normal'))
	mensaje.pack()

boton = Button(app, text='Leer Archivo', command= mostrarArchivo)

boton.pack()
app.mainloop()

