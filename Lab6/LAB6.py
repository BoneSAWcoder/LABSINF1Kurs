import tkinter
import tkinter.ttk
import matplotlib.pyplot
import LAB6EX1
from tkinter import *
window = Tk()
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def EX1():
    LAB6EX1.smt(txt.get())

btn = Button(window, text="Кнопка",bg="green", fg="red", command = EX1) 
btn.grid(column=0, row=0)
window.mainloop()