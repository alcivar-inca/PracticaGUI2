from tkinter import *
app=Tk()
app.title("Aplicacion grafica en Python")
etiqueta = Label (app, text="Hola que hace..??")
boton=Button(app, text="OK")

etiqueta.pack()
boton.pack()
app.mainloop()