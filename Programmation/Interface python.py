# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:51:09 2022

@author: CHARLOT
"""
from tkinter import *
import webbrowser
def kattis():
     webbrowser.open_new("https://open.kattis.com")
window = Tk()
window.title('CHARLOT')
window.geometry("1200x720")
window.minsize(720,360)
window.resizable(width = False,height = False)
window.config(background='white')

frame=Frame(window,bg='white')

label=Label(frame,text="Bienvenue Chez CHARLOT",font=("Arial",40),bg="white",fg="green")
label.pack()
labels=Label(frame,text="Hey salut à tous c'est Joel",font=("Arial",25),bg="white",fg="green")
labels.pack()
button=Button(frame,text="Ouvrir Kattis",font=("Arial",25),bg="white",fg="green",command=kattis)
button.pack(pady=25,fill=X)

frame.pack(expand=YES)
window.mainloop()