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
        if barrier_num < barrier_chance and i % 4 == 0:
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

wn.mainloop()