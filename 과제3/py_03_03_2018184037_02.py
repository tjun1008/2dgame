import turtle

turtle.penup()
turtle.goto(0,250)
for i in range(100,601,100):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,250-i)

turtle.penup()
turtle.goto(0,250)
turtle.right(90)
for i in range(100,601,100):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0+i,250)

turtle.exitonclick()
