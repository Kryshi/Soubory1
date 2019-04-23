# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:52:08 2019

@author: KrySt
"""

from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

#Funkce pro otevírání souboru
def Open():
    
    text.delete(1.0,END)
    route=fd.askopenfilename(title="Open file")
    try:
        file=open(route,"r")
        for line in file:
            text.insert(END,line)
        file.close()
    except:
        pass

#Funkce pro ukládání
def Save():
    
    f=fd.asksaveasfile(title="Save file",defaultextension="txt")
    try:
        textf = str(text.get(1.0, END))
        f.write(textf)
        f.close()
    except:
        pass


#Funkce pro ukončení aplikace
def Kill():
    
    x=mb.askyesno("Exit","Do you want to quit?")
    if x:
        main.destroy()
 

#Funkce pro velká písmena
def Capitalise():
    
    a=text.get(1.0,END)
    a=a.upper()
    
    text.delete(1.0,END)
    text.insert(1.0,a)
   
#funkce pro otevření okna Nahrazení znaku
def Replace():
    
    global origin
    global replacement
    global replacementwindow
    
    replacementwindow=Toplevel()
    replacementwindow.title("Replace character")
    
    t1=Label(replacementwindow,text="Replace character: ")
    t1.pack(pady=3)
    
    origin=Entry(replacementwindow)
    origin.pack(pady=3)
    
    t2=Label(replacementwindow,text="With this: ")
    t2.pack(pady=3)
    
    replacement=Entry(replacementwindow)
    replacement.pack(pady=3)
    
    execute=Button(replacementwindow,command=Rewrite,text="Do it!",width=10)
    execute.pack(pady=3)
    
def Rewrite():
    var = text.get(1.0,END)
    var = str.replace(var, origin.get(), replacement.get())
    text.delete(1.0,END)
    text.insert(1.0,var)
    
def Statistics():
    pass
        

main=Tk()

abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Vzhled aplikace
text=Text(main,font="Arial10")
text.pack()

#hlavní lišta
hornimenu=Menu(main)
#tlačítko FILE
menusoubor=Menu(hornimenu,tearoff=0)

hornimenu.add_cascade(label="File",menu=menusoubor)

menusoubor.add_command(label="Open file",command=Open)

menusoubor.add_command(label="Save file",command=Save)

menusoubor.add_separator()

menusoubor.add_command(label="Exit",command=Kill)

#tlačítko EDIT
menuoperace=Menu(hornimenu,tearoff=0)

hornimenu.add_cascade(label="Edit tools",menu=menuoperace)

menuoperace.add_command(label="Capitalise",command=Capitalise)

menuoperace.add_command(label="Replace",command=Replace)

menuoperace.add_command(label="Statistics",command=Statistics)

menuoperace.add_command(label="Generate text")


main.config(menu=hornimenu)



main.mainloop()