from turtle import *
t1 = Turtle()
t2 = Turtle()
t3= Turtle()
t1.color('green')
t1.begin_fill()
t1.rt(180)
t1.fd(200)
t1.rt(120)
t1.fd(300)
t1.rt(120)
t1.fd(300)
t1.rt(120)
t1.fd(120)
t1.end_fill()
t1.color("brown")
t1.begin_fill()
t1.lt(90)
t1.fd(100)
t1.rt(90)
t1.fd(60)
t1.rt(90)
t1.fd(100)
t1.end_fill()
t2.penup()
t2.goto(-100,255)
t2.pendown()
t2.color('yellow')
t2.begin_fill()
t2.fd(100)
t2.lt(210)
t2.fd(100)
t2.lt(210)
t2.fd(100)
t2.lt(210)
t2.fd(100)
t2.lt(225)
t2.fd(100)
t2.end_fill()
write("MerryX'mas",align="center", font=32)
done()