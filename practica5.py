# -*- coding: utf-8 -*-

from tkinter import *

def DrawList():
	plist=['uno', 'dos', 'tres']

	for item in plist:
		listbox.insert(END, item)

root = Tk()

listbox=Listbox(root)
boton = Button(root, text='Precionar', command = DrawList)

boton.pack()
listbox.pack()
root.mainloop()