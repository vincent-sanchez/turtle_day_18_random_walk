import turtle
from turtle import Turtle
from turtle import Screen
import random
from data import COLORS

# Define width and height of screen
WIDTH, HEIGHT = 500, 500

#Create variables to store position of turtle object
x,y = turtle.position()

# Function that moves Turtle object.
def move():
    tim.forward(10)
    # If tim is either -250 or 250 in x,y, turn 180 left and move forward
    if not -WIDTH/2 < x < WIDTH/2 or not -HEIGHT/2 <y< HEIGHT/2:
        tim.undo()
        tim.left(180)
        tim.forward(10)

def turn():
    angle = random.randint(1,4)
    tim.right(angle*90)

def changeColor():
    tim.color(COLORS[color])

# Create Turtle Object named tim and move tim to the top, middle of the canvas
tim = Turtle()
tim.speed("fastest")

# Move tim for 10000 times
for x in range(0, 10000):
    color = random.randint(0, 478)
    move()
    turn()
    changeColor()

# Create Screen object
screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.exitonclick()
