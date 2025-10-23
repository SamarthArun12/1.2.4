import turtle as trtl
import random

wn = trtl.Screen()

maze_draw = trtl.Turtle()
dist = 20
steps = 2
barrier_chance = 10
maze_draw.speed(0)
maze_draw.right(270)
maze_draw.forward(dist)
while steps < 31:
    for i in range(1, steps):
        door_random = random.randint(1, 4)
        if door_random == 1:
            maze_draw.penup()
        else:
            Barrier_random = random.randint(barrier_chance, 100)   
            if Barrier_random == 1:
                maze_draw.right(270)
                maze_draw.forward(dist*2)
                maze_draw.right(180)
                maze_draw.forward(dist*2)
                maze_draw.right(270)
        maze_draw.forward(dist)
        maze_draw.pendown()
    maze_draw.right(270)
    steps += 1
    if steps % 5 == 0:
        barrier_chance -= 1

maze_draw.hideturtle()

wn.mainloop()
