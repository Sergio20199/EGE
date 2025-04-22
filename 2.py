from turtle import *
k = 20
tracer(0)
screensize(10000,10000)
for i in range(4):
    fd(36*k)
    rt(90)
    fd(41*k)
    rt(90)
penup()
rt(90)
fd(20*k)
lt(90)
fd(20*k)
pendown()
for i in range(4):
    fd(25*k)
    rt(90)
penup()
fd(7*k)
lt(90)
fd(7*k)
rt(90)
pendown()
for i in range(7):
    fd(16*k)
    rt(90)
x = -40
y = -320
penup()
goto(x,y)
for x in range(-20,50):
    for y in range(-50,10):
        goto(x*k,y*k)
        dot(5,"red")
exitonclick()