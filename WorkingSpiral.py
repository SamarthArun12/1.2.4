import turtle as trtl

wn = trtl.Screen()

turt = trtl.Turtle()
dist = 20
turt.speed(0)
while dist < 600:
    turt.right(270)
    turt.forward(dist)
    dist += 20

wn.mainloop()
