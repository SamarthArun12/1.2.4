import turtle as trtl

wn = trtl.Screen()

maze_draw = trtl.Turtle()
dist = 20
steps = 2
maze_draw.pensize(5)
maze_draw.speed(0)
maze_draw.right(270)
maze_draw.forward(dist)

def wall_draw():
    maze_draw.forward(dist)
    maze_draw.pendown()

def barrier_draw():
    maze_draw.right(270)
    maze_draw.forward(dist*2)
    maze_draw.right(180)
    maze_draw.forward(dist*2)
    maze_draw.right(270)


while steps < 31:
    for i in range(1, steps):
        if i % 10 > 5 and i % 10 < 7:
            barrier_draw()
        if i % 10 < 2:
            maze_draw.penup()
        wall_draw()
    maze_draw.right(270)
    steps += 1

maze_draw.hideturtle()

wn.mainloop()