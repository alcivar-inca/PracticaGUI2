import sys
from tkinter import *

def hacer_Click():
	try:
		_valor=int(entrada_texto.get())
		_valor = _valor*5
		etiqueta.config(txt=_valor)
	except ValueError:
		etiqueta.config("Introduce un numero")

app = Tk()
app.title("Mi segunda aplicacion grafica en Python")

# Ventana principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50),pady=(10,10))
vp.columnconfigure(0, weight =1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Valor")
etiqueta.grid(column=2, row= 2, sticky=(W,E))

boton= Button(vp, text="OK", command = hacer_Click)
boton.grid(column=1, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

app.mainloop()