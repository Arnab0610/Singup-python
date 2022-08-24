from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


window=Tk()
window.title("singup")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

img = PhotoImage(file="photo1.PNG")
Label(window,image=img,border=0,bg='white').place(x=50,y=90)

frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sing up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)



def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')



user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)



def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')

password = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)



def on_enter(e):
    conform_code.delete(0,'end')

def on_leave(e):
    name=conform_code.get()
    if name=='':
        conform_code.insert(0,'Conform Password')

conform_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


Button(frame,width=39,pady=7,text='Singup',bg='#57a1f8',fg='white',border=0,).place(x=35,y=280)
Label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',10))
Label.place(x=75,y=340)

Singin = Button(frame,width=6,text='Singin',border=0,bg='white',cursor='hand2',fg='#57a1f8')
Singin.place(x=200,y=340)







window.mainloop()