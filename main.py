from turtle import Turtle, Screen
from random import randint


t = Turtle()
#t.speed(0)

#draw tree trunk
t.color("brown")
t.begin_fill()
t.fd(25)
t.right(90)
t.fd(50)
t.right(90)
t.fd(25)
t.right(90)
t.fd(50)
t.end_fill()

#draw tree
t.penup()
t.goto(-50,0)
t.pendown()
t.right(90)

t.color("green")
t.begin_fill()

for i in range(3):
  t.fd(125)
  t.left(120)
t.end_fill()

for i in range(10):
  x = randint(-50, 50)
  y = randint(0,50)
  t.penup()
  t.goto(x,y)
  colors = ['red','blue']
  t.dot(5, colors[i % len(colors)])

print(t.pos())