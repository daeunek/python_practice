# This program displays n Olympic symbol of five rings of the same size.
import turtle

gap = 20                               #constant gap between circles

turtle.hideturtle()

# user input
radius = float(input("Enter the radius of the ring:"))


# Draw Blue Circle
turtle.color("blue")
turtle.circle(radius)

# Change the position of turtle
turtle.penup()
turtle.forward((2*radius) + gap)
turtle.pendown()

#Draw Black Circle
turtle.color("black")
turtle.circle(radius)

# Change the position of turtle
turtle.penup()
turtle.forward((2*radius) + gap)
turtle.pendown()


#Draw Red Circle
turtle.color("red")
turtle.circle(radius)

# Change the position of turtle
turtle.penup()
turtle.backward(radius + (gap/2))
turtle.right(90)
turtle.forward(radius)
turtle.left(90)
turtle.pendown()

# Draw yellow Circle
turtle.color("yellow")
turtle.circle(radius)

# Change the position of turtle
turtle.penup()
turtle.backward((2*radius) + gap)
turtle.pendown()

#Draw green Circle
turtle.color("green")
turtle.circle(radius) 
           
turtle.done()