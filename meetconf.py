import turtle
from turtle import*#to give u acces to the codes without turtle.balablablablalba
turtle.shape("circle")#change the shape of the turtle

turtle.speed(2)
def square(x,y):
   
    turtle.fillcolor("red")
    turtle.begin_fill()
    fillcolor("red")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+100)
    turtle.goto(x+100,y+100)
    turtle.goto(x+100,y)
    turtle.goto(x,y)
    turtle.end_fill()
    #square

def something(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.down()
    turtle.goto(x+100,y)
    turtle.goto(x+50,y+100)
    turtle.goto(x,y)
#shape2
    
def circle():
  
    turtle.dot(50)

def clear():
    turtle.clear()
    
def change_color_blue():
        turtle.pencolor("blue")
        turtle.color("blue")

turtle.onkey(change_color_blue,"b")

turtle.onscreenclick(square , 1 , True)
turtle.onscreenclick(something, 3 ,True)
turtle.getscreen().onkeypress(clear , "c")
turtle.getscreen().onkeypress(circle,"z")
turtle.getscreen().listen()
turtle.mainloop()
