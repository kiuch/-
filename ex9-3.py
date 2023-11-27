import tkinter as tk
current_number = 0
first_term = 0
second_term = 0
result = 0
operation=1,2,3

def do_plus():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0
def do_minus():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0

def do_times():
    global current_number
    global first_term

    first_term = current_number
    current_number = 0

def do_divide():
   global current_number
   global first_term
   first_term = current_number
     current_number = 0

def do_eq():
    global second_term
    global result
    global current_number
    if operation==1:
        second_term = current_number
        result = first_term + second_term
        current_number = 0
    elif operation==2:
        second_term = current_number
        result = first_term - second_term
        current_number = 0
    elif operation==3:
        second_term = current_number
        result = first_term * second_term
        current_number = 0
    else:
        second_term = current_number
        result = first_term / second_term
        current_number = 0


def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global current_number
    current_number = 0
    show_number(current_number)

def plus():
    do_plus()
    show_number(current_number)
    
def minus():
    do_minus()
    show_number(current_number)

def times():
    do_times()
    show_number(current_number)

def divide():
    do_divide()
    show_number(current_number)

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

root = tk.Tk()
f = tk.Frame(root)
f.grid()

b1 = tk.Button(f,text='1', command=lambda:key(1))
b2 = tk.Button(f,text='2', command=lambda:key(2))
b3 = tk.Button(f,text='3', command=lambda:key(3))
b4 = tk.Button(f,text='4', command=lambda:key(4))
b5 = tk.Button(f,text='5', command=lambda:key(5))
b6 = tk.Button(f,text='6', command=lambda:key(6))
b7 = tk.Button(f,text='7', command=lambda:key(7))
b8 = tk.Button(f,text='8', command=lambda:key(8))
b9 = tk.Button(f,text='9', command=lambda:key(9))
b0 = tk.Button(f,text='0', command=lambda:key(0))
bc = tk.Button(f,text='C', command=clear)
bp = tk.Button(f,text='+', command=plus)
be = tk.Button(f,text='=', command= eq)
bm = tk.Button(f,text='-', command= minus)
bt = tk.Button(f,text='*', command=times)
bd = tk.Button(f,text='/', command=divide)


b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bc.grid(row=1,column=4)
be.grid(row=4,column=2)
bp.grid(row=4,column=3)
bm.grid(row=3,column=3)
bt.grid(row=2,column=3)
bd.grid(row=1,column=3)

e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

root.mainloop()
