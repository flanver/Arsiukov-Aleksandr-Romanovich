from tkinter import *  
from tkinter import messagebox
import tkinter as tk 
import tkinter
import requests
import json


def clicked():  
    v = txt.get()
    response = requests.get('https://api.github.com/users/OwnCloud')

    f_ = json.loads(response.text)

    y = dict.fromkeys(['company'], f_['company'])
    y2 = dict.fromkeys(['created_at'], f_['created_at'])
    y3 = dict.fromkeys(['email'], f_['email'])
    y4 = dict.fromkeys(['id'], f_['id'])
    y5 = dict.fromkeys(['name'], f_['name'])
    y6 = dict.fromkeys(['url'], f_['url'])
    j = (y,y2,y3,y4,y5,y6)




    

    if v == 'OwnCloud':
        with open('C:\\Users\\fotog\\Desktop\\работы инфа\\Arsiukov-Aleksandr-Romanovich\\пр 11\\пр 11 репозиторий 50\\vivod.json', 'w') as file:
            json.dump(j,file)
        messagebox.showwarning('предупреждение', 'файл был сохранен')
        window.destroy()
        
        
    else:
        messagebox.showwarning('ошибка', 'Пользователь не найден')
    
    


window = Tk()  
window.title("Добро пожаловать ")  
window.geometry('400x250')  
lbl = Label(window, text="Введите имя пользователя")  
lbl.grid(column=200, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=200, row=12)  
btn = Button(window, text="Готово!!", command=clicked)  
btn.grid(column=200, row=25)  
window.mainloop()


