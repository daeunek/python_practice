## This Program displays a triangle and its area.
import turtle
import math
turtle.hideturtle()

# Prompt the user for inputting three points of a triangle
x1, y1 = eval(input("Enter x1 and y1 for p1 (eg. x1,y1): "))
x2, y2 = eval(input("Enter x2 and y2 for p2 (eg. x2,y2): "))
x3, y3 = eval(input("Enter x3 and y3 for p3 (eg. x3,y3): "))

# Compute the sides of a triangle
s1 = math.sqrt((x2-x1)**2 +(y2-y1)**2)
s2 = math.sqrt((x3-x2)**2 +(y3-y2)**2)
s3 = math.sqrt((x3-x1)**2 +(y3-y1)**2)

# side 1
turtle.penup()
turtle.goto(x1,y1)            # Move to p1
turtle.pendown()
turtle.write("p1")
turtle.goto(x2,y2)
turtle.write("p2")            # Move to p2 and form side 1

#side 2
turtle.goto(x3,y3)             #Move to P3 and form side 2
turtle.write("p3")

#side 3
turtle.goto(x1,y1)           #Move to p1 and form side 3

# Compute the area
s = (s1 + s2 + s3)/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

tri_area = "Area of a triangle: {:.2f} ".format(area)

# write the area below triangle
turtle.penup()
turtle.sety(-100) 
turtle.pendown()
turtle.write(tri_area)

turtle.done()