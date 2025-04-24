# ###############################################
# ### SETUP ###
import turtle
# ###############################################
#directions for turtle
t = turtle.Turtle()
t.penup()
t.goto(0, -100)
t.color("blue")
t.pendown()
#color of backround and pen
t.color("purple")
turtle.Screen() .bgcolor("black")

#repeat directions
for i in range(100):
    t.forward(100 + i)
    t.left(90)




# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
