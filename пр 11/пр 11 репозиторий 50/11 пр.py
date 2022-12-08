from tkinter import *  
from tkinter import messagebox
import tkinter
import requests
import json


def clicked():  
    res = "Привет ".format(txt.get())  
    lbl.configure(text=res)  
    messagebox.showwarning('предупреждение', 'файл будет сохранен как только вы нажмете Ок')
    return txt.get()
def com():
    with open ("C:\\Users\\fotog\\Desktop\\работы инфа\\Arsiukov-Aleksandr-Romanovich\\пр 11\\пр 11 репозиторий 50\\ddd.txt", 'w') as file:
        file.write(str(clicked()))
    window.destroy()
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
lbl = Label(window, text="Привет")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Клик!", command=com)  
btn.grid(column=2, row=0)  
window.mainloop()

