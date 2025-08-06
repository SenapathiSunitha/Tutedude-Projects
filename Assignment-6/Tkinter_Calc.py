from tkinter import *
window=Tk()
window.geometry('500x500')
window.title("Calculator")
e=Entry(window, width=56, borderwidth=5)
e.place(x=0,y=0)
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+ str(num))
b=Button(window,text='1',width=12, command=lambda:click(1), bg="grey")
b.place(x=10,y=60)
b=Button(window,text='2',width=12, command=lambda:click(2), bg="grey")
b.place(x=80,y=60)
b=Button(window,text='3',width=12, command=lambda:click(3), bg="grey")
b.place(x=170,y=60)
b=Button(window,text='4',width=12, command=lambda:click(4), bg="grey")
b.place(x=10,y=120)
b=Button(window,text='5',width=12, command=lambda:click(5), bg="grey")
b.place(x=80,y=120)
b=Button(window,text='6',width=12, command=lambda:click(6), bg="grey")
b.place(x=170,y=120)
b=Button(window,text='7',width=12, command=lambda:click(7), bg="grey")
b.place(x=10,y=180)
b=Button(window,text='8',width=12, command=lambda:click(8), bg="grey")
b.place(x=80,y=180)
b=Button(window,text='9',width=12, command=lambda:click(9), bg="grey")
b.place(x=170,y=180)
b=Button(window,text='0',width=12, command=lambda:click(0), bg="grey")
b.place(x=10,y=240)
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0,END)
b=Button(window,text='+',width=12, command=add, bg="lavender",cursor="hand2")
b.place(x=80,y=240)
def sub():
    n1=e.get()
    global math
    math = "subtraction"
    global i
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='-',width=12, command=sub, bg="lavender",cursor="hand2")
b.place(x=170,y=240)
def mul():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='*',width=12, command=mul, bg="lavender",cursor="hand2")
b.place(x=10,y=300)
def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i=int(n1)
    e.delete(0, END)
b=Button(window,text='/',width=12, command=div, bg="lavender",cursor="hand2")
b.place(x=80,y=300)
def eql():
    n2=e.get()
    e.delete(0,END)
    if(math=="addition"):
        e.insert(0,i+int(n2))
    elif(math=="subtraction"):
        e.insert(0,i-int(n2))
    elif(math=="multiplication"):
        e.insert(0,i*int(n2))
    elif(math=="division"):
        e.insert(0,i/int(n2))
b=Button(window,text='=',width=12, command=eql, bg="sky blue",cursor="hand2")
b.place(x=170,y=300)
def clr():
    e.delete(0,END)
b=Button(window,text='clear',width=12, command=clr, bg="red",cursor="cross")
b.place(x=10,y=350)
window.mainloop()
