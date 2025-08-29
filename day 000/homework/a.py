from turtle import *

width(5)
speed(6)
color("green")

penup()
goto(-200,0)
pendown()
begin_fill()
forward(600)
right(90)
forward(200)
right(90)
forward(600)
right(90)
forward(200)
right(90)
end_fill()


#house begin

color("red")
penup()
goto(0,0)
pendown()

forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(80)


#door start



left(90)
forward(60)

right(90)
forward(40)

right(90)
forward(60)

penup()
goto(110,30)
pendown()
color("black")
forward(1)

#door end

color("red")
penup()
goto(200,200)
pendown()

begin_fill()

right(150)
forward(200)

left(120)
forward(200)
end_fill()
#house end

#windows start
color("blue")
penup()
goto(40,100)
pendown()


left(120)
forward (40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()
goto(120,100)
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(20)

left(90)
forward(40)

penup()
goto(60,100)
pendown()

forward(40)


#windows end

exitonclick()