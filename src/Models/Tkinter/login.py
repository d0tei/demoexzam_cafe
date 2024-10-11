from tkinter import *

from src.Controllers.UserController import *

def click_test():
    button_login.configure(text ="Нажал")
    message.configure(text = "Нажал", font=(16),foreground ='red')
    log_in.selection_clear()
def login():
    user = UserController()
    result = user.log_in(log_in.get(),passwd_in.get())
    if result:
        log = UserController.show(log_in.get()).role_id.id
        if log == 1:
            print("Admin")
        elif log==2:
            print("Cook")
        else:
            print("Oficiant")
    else:
        print("Логин ли пароль введем не верно")
    print(result)
window = Tk()
window.title("Информационная система КАФЕ")
window.geometry('700x600')
title = Label(window,text="Приветствуем в информационной системе КАФЕ",font=("Times New Roman",16))
title.grid(column = 0, row = 0)

button_login =Button(window,
                     text="Войти",
                     height=1,
                     width=5,
                     background='green',
                     foreground='white',
                     command=login)
button_login.grid(column = 0, row =1)
message = Label(text='!!!')
message.grid(column =0,row =4)

log_title = Label(window,text="Введите логин")
log_title.grid(column=0,row=5)
log_in = Entry(window,width=20)
log_in.grid(column=1,row=5)
passwd_title = Label(window,text="Введите пароль")
passwd_title.grid(column=0,row=6)
passwd_in = Entry(window,width=20)
passwd_in.grid(column=1,row=6)



window.mainloop()