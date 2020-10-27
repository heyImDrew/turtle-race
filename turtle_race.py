import turtle
import threading
import random

screen = turtle.Screen()
screen.title("TURTLE RACE")
screen.setup(640,480)
screen.setworldcoordinates(-1, -1, 50, 50)

screen.clear()
turtles = {}
position = [25, 0]
colors = ['#B22222', '#D2691E', '#008000', '#4B0082', '#0000FF']
for i in range(0, 5):
    temp_turtle = turtle.Turtle(shape="turtle", visible=False)
    temp_turtle.color(colors[i])
    temp_turtle.speed(2)
    temp_turtle.pencolor('#FFFFFF')
    temp_turtle.showturtle()
    temp_turtle.goto(position[0], position[1])
    position[0] -= 5
    turtles[i] = temp_turtle
for i in range(0, 5):
    turtles[i].left(90)

coord = [32, 30]
pen = turtle.Turtle(visible=False)
pen.speed(100)
pen.fillcolor('#f3f3f3')
pen.penup()
pen.goto(coord[0], coord[1])
pen.pendown()
pen.begin_fill()
pen.goto(coord[0]+14, coord[1])
pen.goto(coord[0]+14, coord[1]+5)
pen.goto(coord[0], coord[1]+5)
pen.goto(coord[0], coord[1])
pen.end_fill()
pen.penup()
pen.goto([coord[0]+1,coord[1]+1])
pen.pendown()
pen.write("Click here to start!", font=("Arial", 14, "normal"))

finish = turtle.Turtle(visible=False)
finish.speed(100)
finish.penup()
finish.goto(1, 30)
finish.pendown()
finish.begin_fill()
finish.goto(30, 30)
finish.end_fill()
finish.penup()

run = False

def race():
    run = True
    winner = -1
    while(run):
        for i in range(0,5,1):
            turtles[i].forward(random.randrange(1,3))
            if turtles[i].position()[1] > 30:
                run = False
                if winner == -1:
                    winner = i
                    if winner == 0:
                        print("red is a winner")
                    elif winner == 1:
                        print("orange is a winner")
                    elif winner == 2:
                        print("green is a winner")
                    elif winner == 3:
                        print("purple is a winner")
                    elif winner == 4:
                        print("blue is a winner")

def btnclick(x,y):
    if x > 32 and x < 46 and y < 35 and y > 30:
        for i in range(0, 10):
            pen.undo()
        race()

turtle.onscreenclick(btnclick)
turtle.listen()

turtle.done()