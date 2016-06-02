from tkinter import *
app = Tk()
app.geometry('600x400+350+70')

def mostrarArchivo():
	archivo = open('textoAgenda.txt', 'r')
	linea=archivo.read()
	archivo.close()
	texto=linea.split(';')
	listb = Listbox(app)
	listb.pack()
	for item in texto:
		listb.insert(0, item)

	# mensaje = Message(app, text=listb)
	# mensaje.config(bg = 'lightgreen', font=('arial', 20, 'normal'))
	# mensaje.pack()

boton = Button(app, text='Leer Archivo', command= mostrarArchivo)

boton.pack()
app.mainloop()