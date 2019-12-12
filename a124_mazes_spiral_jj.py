#an import for the turtle to draw the maze
import turtle as trtl 
import random 

#renaming the turtle to a better name to identify it
maze_bot = trtl.Turtle()
maze_bot.ht()
billy_bob_thornton = trtl.Turtle()

#a different color for the turtle
maze_bot.color("green")
billy_bob_thornton.penup()
billy_bob_thornton.setposition(185,315)
billy_bob_thornton.pendown()

amount = 25
wall_width = 25
maze_bot.speed(0)
maze_bot.pensize(5)
door_width = 30
barrier = 30


#code for the range of the maze
for i in range(25):
    if i > 4 and i < 22:
        barrier = random.randint(2*wall_width, amount - 2*wall_width)
        door = random.randint(2*wall_width, amount - 2*wall_width)

        if door < barrier:
            maze_bot.forward(door)
            maze_bot.penup()
            maze_bot.forward(door_width)
            maze_bot.pendown()
            maze_bot.forward(barrier - door - door_width)

            maze_bot.left(90)
            maze_bot.forward(wall_width*2)
            maze_bot.back(wall_width*2)
            maze_bot.right(90)

            maze_bot.forward(amount - barrier)
        else:
            maze_bot.forward(barrier)
            maze_bot.left(90)
            maze_bot.forward(wall_width*2)
            maze_bot.back(wall_width*2)
            maze_bot.right(90)

            maze_bot.forward(door - barrier)

            maze_bot.penup()
            maze_bot.forward(door_width)
            maze_bot.pendown()            

            maze_bot.forward(amount - door - door_width)


    maze_bot.left(90)
    amount += wall_width

def up():
    billy_bob_thornton.setheading(90)
    billy_bob_thornton.forward(5)

def down():
    billy_bob_thornton.setheading(270)
    billy_bob_thornton.forward(5)
def left():
    billy_bob_thornton.setheading(180)
    billy_bob_thornton.forward(5)
def right():
    billy_bob_thornton.setheading(0)
    billy_bob_thornton.forward(5)



wn = trtl.Screen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.listen()
wn.bgcolor("saddlebrown")
wn.mainloop()