#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import ImageGrab

pencere = Tk()
def ssal():
	pencere.iconify()
	dosya = "resim.png"
	ImageGrab.grab().save(dosya)

dugme = Button(text="SS AL!", command=ssal)
dugme.pack()
mainloop()
