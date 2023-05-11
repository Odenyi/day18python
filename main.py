import random
# from turtle import Turtle,Screen
import turtle as t

tim =t.Turtle()
t.colormode(255)
# tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# draw dots
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# draw shapes from 3 to 10
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
color = ["steel blue","light sea green" ,"sienna","blue","orange","dark cyan","deep pink",]
# def drawshape(number_of_sides):
#     angle = 360/number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape in range(3,11):
#     tim.color(random.choice(color))
#     drawshape(shape)
#random walk path
#draw a random path

def choose_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    mytyple = (r,g,b)
    return mytyple
direction = [0,90,180,270]
tim.speed("fastest")
for _ in range(200):
    tim.width(_/50)
    tim.color(choose_color())
    tim.forward(10)
    tim.setheading(random.choice(direction))
















screen = t.Screen()
screen.exitonclick()