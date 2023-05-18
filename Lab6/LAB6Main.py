import tkinter
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter.ttk import Checkbutton
import matplotlib.pyplot
import LAB6EX1
import LAB6EX2
import LAB6EX3
from tkinter import *
window = Tk()
tab_control = ttk.Notebook(window) 
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='EX1') 
tab_control.add(tab2, text='EX2')
tab_control.add(tab3, text='EX3') 
tab_control.pack(expand=1, fill='both') 
#TAB1
TAB1txt1 = Entry(tab1, width=10)
TAB1txt1.grid(column=0, row=0)
TAB1txt2 = Entry(tab1, width=10)
TAB1txt2.grid(column=1, row=0)
TAB1txt3 = Entry(tab1, width=10)
TAB1txt3.grid(column=2, row=0)
#TABLables
TAB1Lbl1 = Label(tab1, text="Xmin")
TAB1Lbl1.grid(column=0, row=1)
TAB1Lbl2 = Label(tab1, text="Xmax")
TAB1Lbl2.grid(column=1, row=1)
TAB1Lbl3 = Label(tab1, text="Function")
TAB1Lbl3.grid(column=2, row=1)
#TAB1Func
def Ex1():
    LAB6EX1.MakeGraph(TAB1txt3.get(), int(TAB1txt1.get()), int(TAB1txt2.get()))
btn = Button(tab1, text="Make Graph", command = Ex1) 
btn.grid(column=3, row=0)

#TAB2
NumberStud = LAB6EX2.ReturnNumber()
Buttonlist = list()
Radval = IntVar()
Radval.set(0)
for i in range(0,NumberStud):
    Buttonlist.append(Radiobutton(tab2, text = LAB6EX2.ReturnName(i), value = i, variable = Radval))
    Buttonlist[i].grid(column=0, row=i)

MathCheck = BooleanVar()
InfaCheck = BooleanVar()
RusslangCheck = BooleanVar()
MathCheck.set(0)
InfaCheck.set(0)
RusslangCheck.set(0)
MathCheckbutton = Checkbutton(tab2, text = 'Math',variable = MathCheck, offvalue=0, onvalue=1)
MathCheckbutton.grid(column=1,row=0)
InfaCheckbutton = Checkbutton(tab2, text = 'Informatics',variable=InfaCheck, offvalue=0, onvalue=1)
InfaCheckbutton.grid(column=1,row=1)
RussLangCheckbutton = Checkbutton(tab2, text = 'Russian Language',variable=RusslangCheck, offvalue=0, onvalue=1)
RussLangCheckbutton.grid(column=1,row=2)

TAB2txt1 = Entry(tab2, width=10)
TAB2txt1.grid(column=3, row=0)
TAB2txt2 = Entry(tab2, width=10)
TAB2txt2.grid(column=3, row=1)
TAB2txt3 = Entry(tab2, width=10)
TAB2txt3.grid(column=3, row=2)

def Ex2():
    if MathCheck.get() == 1:
        LAB6EX2.RewriteScore(Radval.get(),'Math',TAB2txt1.get())
    if InfaCheck.get() == 1:
        LAB6EX2.RewriteScore(Radval.get(),'Inform',TAB2txt2.get())
    if RusslangCheck.get() == 1:
        LAB6EX2.RewriteScore(Radval.get(),'RusLang',TAB2txt3.get())

btn2 = Button(tab2, text="UDP XML", command = Ex2) 
btn2.grid(column=0, row=5)




#TAB3
TAB3Lbl1 = Label(tab3, text="Surname")
TAB3Lbl1.grid(column=0, row=0)
TAB3Lbl2 = Label(tab3, text="Math")
TAB3Lbl2.grid(column=0, row=1)
TAB3Lbl3 = Label(tab3, text="Informatics")
TAB3Lbl3.grid(column=0, row=2)
TAB3Lbl4 = Label(tab3, text="Russian Language")
TAB3Lbl4.grid(column=0, row=4)


TAB3txt1 = Entry(tab3, width=10)
TAB3txt1.grid(column=2, row=0)
TAB3txt2 = Entry(tab3, width=10)
TAB3txt2.grid(column=2, row=1)
TAB3txt3 = Entry(tab3, width=10)
TAB3txt3.grid(column=2, row=2)
TAB3txt4 = Entry(tab3, width=10)
TAB3txt4.grid(column=2, row=3)

def Ex3():
    LAB6EX3.AddStudent(str(NumberStud),TAB3txt1.get(),TAB3txt2.get(),TAB3txt3.get(),TAB3txt4.get())
btn3 = Button(tab3, text="UDP XML", command = Ex3) 
btn3.grid(column=0, row=5)
window.mainloop()