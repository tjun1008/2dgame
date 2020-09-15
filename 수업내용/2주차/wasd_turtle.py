import turtle

def w_turtle():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def a_turtle():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def s_turtle():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def d_turtle():
    turtle.setheading(360)
    turtle.forward(50)
    turtle.stamp()

def reset_turtle():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(w_turtle,'w')
turtle.onkey(a_turtle,'a')
turtle.onkey(s_turtle,'s')
turtle.onkey(d_turtle,'d')
turtle.onkey(reset_turtle,'Escape')
turtle.listen()

