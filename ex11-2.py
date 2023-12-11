class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"

    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            print(self.first_term, self.second_term)
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation == "/":
            self.result = self.first_term / self.second_term

dentaku = Dentaku()
kenzan = Dentaku()
while True:
    f = int(input("First term "))
    dentaku.first_term = f
    o = input("Operation ")
    dentaku.operation = o
    s = int(input("Second term "))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result
    print("Result ", r)
   
    kenzan.first_term = r
    kenzan.second_term = s
    if o == "+":
        kenzan.operation = "-"
    elif o == "-":
        kenzan.operation = "+"
    elif o == "*":
        kenzan.operation = "/"
    elif o == "/":
        kenzan.operation = "*"
    kenzan.do_operation()
    k = kenzan.result
    if k == dentaku.first_term:
        print(" OK", k)
    else:
        print(" NG")

