#an import for the turtle to draw the maze
import turtle as trtl 
import random as random

#renaming the turtle to a better name to identify it
maze_bot = trtl.Turtle()
maze_bot.ht()
#a different color for the turtle
maze_bot.color("green")


amount = 25
wall_width = 25
maze_bot.speed(0)
maze_bot.pensize(5)
door_width = 10


#code for the range of the maze
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
