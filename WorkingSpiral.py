import turtle as trtl

wn = trtl.Screen()

maze_drawer = trtl.Turtle()
dist = 20
maze_drawer.speed(0)
while dist < 600:
    maze_drawer.right(270)
    maze_drawer.forward(dist)
    dist += 20
maze_drawer.hideturtle()

wn.mainloop()

