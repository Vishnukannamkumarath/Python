from tkinter import *
from tkinter.ttk import *
t=Tk()
t.geometry('500x500')
style=Style()
style.configure('TButton',font=('calibri',20,'bold'),bd='7')
b1=Button(t,text='7',command=t.destroy)

b1.pack(side='left')
b2=Button(t,text='8',command=t.destroy)
b2.pack(side='left')
b3=Button(t,text='9',command=t.destroy)
b3.pack(side='left')
t.nextLine()
b4=Button(t,text='4',command=t.destroy)
b4.pack(side='left')



t.mainloop()
