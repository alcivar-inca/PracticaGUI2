# -*- coding: utf-8 -*-

from tkinter import *
root = Tk()

li='Primer elemento'.split
listb = Listbox(root)
for item in li:
	listb.insert(0, item)

listb.pack()
root.mainloop()