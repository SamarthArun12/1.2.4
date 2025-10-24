import turtle as trtl

wn = trtl.Screen()

maze_draw = trtl.Turtle()
dist = 20
steps = 2
maze_draw.speed(0)
maze_draw.right(270)
maze_draw.forward(dist)
while steps < 31:
    for i in range(1, steps):
        if i % 10 < 2:
            maze_draw.penup()
        maze_draw.forward(dist)
        maze_draw.pendown()
    maze_draw.right(270)
    steps += 1

maze_draw.hideturtle()

wn.mainloop()
