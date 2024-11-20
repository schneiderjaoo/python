from turtle import *

# Desenhando o coração
color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(0, 50)

color("black")
write("Texto em arial ao centro", align="center", font=("Arial", 16, "bold"))
hideturtle()
done()
