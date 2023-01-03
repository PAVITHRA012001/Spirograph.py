import random
from turtle import Turtle, Screen

spiro = Turtle()
colours=["red","purple","green","yellow","pink"]


spiro.speed("fastest")

def draw(num):
    for _ in range(int(360/num)):
        spiro.color(random.choice(colours))
        spiro.circle(150)
        current_heading = spiro.heading()
        spiro.setheading(current_heading + num)
        spiro.circle(150)

draw(10)
screen = Screen()
screen.exitonclick()