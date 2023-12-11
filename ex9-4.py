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
  second_term = current_number
  
  if operation == 1:
    result = first_term + second_term
  elif operation == 2:
    result = first_term - second_term
  elif operation == 3:
    result = first_term * second_term
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

def divide():
  global operation
  operation = 4
  do_assignment()
  show_number(current_number)

def eq():
  do_eq()
  show_number(result)

def show_number(num):
  e.delete(0, tk.END)
  e.insert(0, str(num))

root = tk.Tk()
f = tk.Frame(root)
f.grid()
f.configure(bg='#ffffc0')

j = list()
for i in range(0, 10):
    j.append(tk.Button(f, text=i, command=lambda x=i: key(x)))
             
bc = tk.Button(f, text = 'C', command = clear, font = ('Helvetica', 14), width = 2, bg = '#ff0000')
bd = tk.Button(f, text = '/', command = divide, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bt = tk.Button(f, text = '*', command = mult, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bm = tk.Button(f, text = '-', command = minus, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
bp = tk.Button(f, text = '+', command = plus, font = ('Helvetica', 14), width = 2, bg = '#00ff00')
be = tk.Button(f, text = '=', command = eq, font = ('Helvetica', 14), width = 2, bg = '#00ff00')

r = 4
c = 0
for i, k in enumerate(j):
    k.grid(row=r, column=c)
    c += 1
    if c > 2 or i == 0:
        c = 0
        r -= 1
    
bc.grid(row=4, column=1)
be.grid(row=4, column=2)
bp.grid(row=1, column=3)
bm.grid(row=2, column=3)
bt.grid(row=3, column=3)
bd.grid(row=4, column=3)

for k in j:
    k.configure(bg='#ffffff', width=2, font=('Helvetica', 14))

bc.configure(bg='#ff0000', width=2, font=('Helvetica', 14))
be.configure(bg='#00ff00', width=2, font=('Helvetica', 14))
bp.configure(bg='#00ff00', width=2, font=('Helvetica', 14))
bm.configure(bg='#00ff00', width=2, font=('Helvetica', 14))
bt.configure(bg='#00ff00', width=2, font=('Helvetica', 14))
bd.configure(bg='#00ff00', width=2, font=('Helvetica', 14))

e = tk.Entry(f)
e.grid(row=0, column=0,columnspan=4)
e.configure(font=('Helvetica', 14))


root.mainloop()
