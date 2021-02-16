import sys

max_length = sys.argv[1]
angle = sys.argv[2]
repeat = sys.argv[3]
dilation = sys.argv[4]

from turtle import * #https://docs.python.org/3.3/library/turtle.html?highlight=turtle

setup(width=.75, height=1.0, startx=None, starty=None)

speed(0)
pencolor()

penup()
lt(90)
fd(100)
rt(90)
pendown()

ht()

def function_one_rotation():
    global x
    for i in range(int(max_length)):
        fd(x * int(dilation))
        rt(180 - int(angle))
        x += 1

global x
for j in range(int(repeat)):
    x = 1
    function_one_rotation()

print('\nDONE\n')
done()
