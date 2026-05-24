from turtle import *
tracer(0)
left(90)
k = 40
for i in range(2):
    rt(120)
    fd(9*k)
rt(300)
for i in range(2):
    rt(120)
    fd(9*k)
pu()
for x in range(-60, 60):
    for y in range(-60,60):
        goto(x *k, y*k)
        dot(5)
done()
