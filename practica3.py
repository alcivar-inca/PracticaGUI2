# -*- coding: utf-8 -*-
from tkinter import *

def call():
	lab=Label(root, text ='Usted preciono un boton')
	lab.pack()

root = Tk()
root.geometry('100x110+350+70')
boton = Button(root, text='Precionar', command=call)
boton.pack()
root.mainloop()