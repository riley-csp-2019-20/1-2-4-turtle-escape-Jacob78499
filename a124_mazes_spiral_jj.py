import turtle as trtl 

maze_bot = trtl.Turtle()
maze_bot.ht()
maze_bot.color("green")

amount = 25
wall_width = 25
maze_bot.speed(0)
maze_bot.pensize(5)

for i in range(25):
    if i < 22:
        maze_bot.forward(amount/3)
        maze_bot.penup()
        maze_bot.forward(wall_width+5)
        maze_bot.pendown()
        maze_bot.forward(40)
        if i > 4:
            maze_bot.left(90)
            maze_bot.forward(wall_width*2)
            maze_bot.back(wall_width*2)
            maze_bot.right(90)
        maze_bot.forward(2*amount/3)
        maze_bot.left(90)
        amount += wall_width
    else:
        amount += wall_width
        maze_bot.forward(amount + wall_width)
        maze_bot.left(90)
       

wn = trtl.Screen()
wn.mainloop()
