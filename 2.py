from turtle import *
k = 35
speed(100)
for i in range(4):
    forward(8*k)
    right(90)
for i in range(3):
    forward(12*k)
    right(120)
penup()
x = -40
y = -320
goto(x,y)
for x in range(0,20):
    for y in range(-10,1):
        goto(x*k,y*k)
        dot(2,"red")
