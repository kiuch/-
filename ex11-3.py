import tkinter as tk

class Dentaku():
    def __init__(self):
        self.current_number = 0
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"

    def do_eq(self):
        self.second_term = self.current_number
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation == "/":
            self.result = self.first_term / self.second_term
        self.current_number = 0
        self.operation = 0

    def key(self, n):
        self.current_number = self.current_number * 10 + n
        self.show_number(self.current_number)

    def calc(self, op):
        self.operation = op
        self.first_term = self.current_number
        self.current_number = 0

    def clear(self):
        self.current_number = 0
        self.show_number(self.current_number)

    def eq(self):
        self.do_eq()
        self.show_number(self.result)

    def show_number(self, num):
        e.delete(0, tk.END)
        e.insert(0, str(num))

dentaku = Dentaku()
root = tk.Tk()
f = tk.Frame(root)
f.grid()
f.configure(bg='#ffffc0')

j = list()
for i in range(0, 10):
    j.append(tk.Button(f, text=i, command=lambda x=i: dentaku.key(x)))
             
bc = tk.Button(f, text='C', command=dentaku.clear)
bp = tk.Button(f, text='+', command=lambda x="+": dentaku.calc(x))
bm = tk.Button(f, text='-', command=lambda x="-": dentaku.calc(x))
bt = tk.Button(f, text='x', command=lambda x="*": dentaku.calc(x))
bd = tk.Button(f, text='÷', command=lambda x="/": dentaku.calc(x))
be = tk.Button(f, text='=', command=dentaku.eq)

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
dentaku.clear()

root.mainloop()
