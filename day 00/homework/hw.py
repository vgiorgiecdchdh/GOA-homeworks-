from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #heght of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(120)
right(120)

#drawing a windows

penup()
goto(15,130)
pendown()

color("green")
left(120)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto(155,130)
pendown()

color("green")
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto(170,130)
pendown()

color("green")
left(180)
forward(30)

penup()
goto(30,130)
pendown()

color("green")
right(360)
forward(30)
right(90)
forward(10)

exitonclick()