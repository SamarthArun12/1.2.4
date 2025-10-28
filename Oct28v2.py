import turtle as trtl
import random as rand

wn = trtl.Screen()

maze_draw = trtl.Turtle()
dist = 20
steps = 2
maze_draw.pensize(5)
maze_draw.speed(0)

def wall_draw():
    maze_draw.forward(dist)
    maze_draw.pendown()

def barrier_draw():
    maze_draw.right(270)
    maze_draw.forward(dist*2)
    maze_draw.right(180)
    maze_draw.forward(dist*2)
    maze_draw.right(270)

barrier_chance = 10
door_chance = 5

maze_draw.right(270)
while steps < 31:
    for i in range(1, steps):
        door_num = rand.randint(1,101)
        barrier_num = rand.randint(1,101)
        if i < 4:
            maze_draw.penup()
        if barrier_num < barrier_chance and i % 2 == 0:
            barrier_draw()
        if door_num < door_chance:
            maze_draw.penup()
        wall_draw()
    maze_draw.right(270)
    steps += 1

    if barrier_chance < 50:
        barrier_chance *= 1.3
    if door_chance < 20:
        door_chance += 2

maze_draw.hideturtle()

maze_run = trtl.Turtle()

def up():
    maze_run.setheading(90)
    maze_run.forward(15)
    if abs(maze_run.xcor()) > 280 or abs(maze_run.ycor()) > 280:
        maze_run.hideturtle()
        maze_run.penup()
        maze_run.clear()
        maze_run.goto(0,0)
        maze_run.showturtle()
        maze_run.pendown()

def down():
    maze_run.setheading(270)
    maze_run.forward(15)
    if abs(maze_run.xcor()) > 280 or abs(maze_run.ycor()) > 280:
        maze_run.hideturtle()
        maze_run.penup()
        maze_run.clear()
        maze_run.goto(0,0)
        maze_run.showturtle()
        maze_run.pendown()
def right():
    maze_run.setheading(0)
    maze_run.forward(15)
    if abs(maze_run.xcor()) > 280 or abs(maze_run.ycor()) > 280:
        maze_run.hideturtle()
        maze_run.penup()
        maze_run.clear()
        maze_run.goto(0,0)
        maze_run.showturtle()
        maze_run.pendown()

def left():
    maze_run.setheading(180)
    maze_run.forward(15)
    if abs(maze_run.xcor()) > 280 or abs(maze_run.ycor()) > 280:
        maze_run.hideturtle()
        maze_run.penup()
        maze_run.clear()
        maze_run.goto(0,0)
        maze_run.showturtle()
        maze_run.pendown()
def speed():
    maze_run.speed(9)

maze_run.penup()
maze_run.showturtle()
maze_run.goto(0,0)
maze_run.pendown()
maze_run.pencolor("blue")

wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(speed, "Shift_L")
wn.listen()



wn.mainloop()
