import tkinter as tk

current_number = 0

first_term = 0
second_term = 0
result = 0
operation = 0

def do_assignment():
  global current_number
  global first_term

  first_term = current_number
  current_number = 0

def do_eq():
  global operation
  global second_term
  global result
  global current_number
  global tax
  tax=first_term*0.1
  second_term = current_number
  
  if operation == 1:
    result = first_term + second_term
  elif operation == 2:
    result = first_term - second_term
  elif operation == 3:
    result = first_term * second_term
  elif operation == 4:
    result = first_term+tax
  else:
    if second_term == 0:
      result = 'error'
    else:
      result = first_term // second_term

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
  global operation
  operation = 1
  do_assignment()
  show_number(current_number)

def minus():
  global operation
  operation = 2
  do_assignment()
  show_number(current_number)

def mult():
  global operation
  operation = 3
  do_assignment()
  show_number(current_number)

def tax():
  global operation
  operation = 4
  do_assignment()
  show_number(current_number)
  
def divide():
  global operation
  operation = 5
  do_assignment()
  show_number(current_number)

def eq():
  do_eq()
  show_number(result)

def show_number(num):
  e.delete(0, tk.END)
  e.insert(0, str(num))

root = tk.Tk()
f = tk.Frame(root, bg = '#ffffc0')
f.grid()

b1 = tk.Button(f, text = '1', command = lambda:key(1), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b2 = tk.Button(f, text = '2', command = lambda:key(2), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b3 = tk.Button(f, text = '3', command = lambda:key(3), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b4 = tk.Button(f, text = '4', command = lambda:key(4), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b5 = tk.Button(f, text = '5', command = lambda:key(5), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b6 = tk.Button(f, text = '6', command = lambda:key(6), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b7 = tk.Button(f, text = '7', command = lambda:key(7), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b8 = tk.Button(f, text = '8', command = lambda:key(8), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b9 = tk.Button(f, text = '9', command = lambda:key(9), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
b0 = tk.Button(f, text = '0', command = lambda:key(0), font = ('Helvetica', 14), width = 2, bg = '#ffffff')
bc = tk.Button(f, text = 'C', command = clear, font = ('Helvetica', 14), width = 2, bg = '#ff0000')
bd = tk.Button(f, text = '/', command = divide, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bt = tk.Button(f, text = '*', command = mult, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bm = tk.Button(f, text = '-', command = minus, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bp = tk.Button(f, text = '+', command = plus, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bx = tk.Button(f, text = '%', command = tax, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
be = tk.Button(f, text = '=', command = eq, font = ('Helvetica', 14), width = 2, bg = '#00ff00')


b1.grid(row = 4, column = 0)
b2.grid(row = 4, column = 1)
b3.grid(row = 4, column = 2)
b4.grid(row = 3, column = 0)
b5.grid(row = 3, column = 1)
b6.grid(row = 3, column = 2)
b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)
b0.grid(row = 5, column = 0)
bc.grid(row = 1, column = 0)
be.grid(row = 6, column = 3)
bd.grid(row = 1, column = 3)
bt.grid(row = 2, column = 3)
bm.grid(row = 3, column = 3)
bx.grid(row = 4, column = 3)
bp.grid(row = 5, column = 3)

e = tk.Entry(f)
e.grid(row = 0, column = 0, columnspan = 4)
clear()

root.mainloop()
