import calendar
import turtle

turtle.tracer(0)

#turtle starts from 0,0

cal_len = 350
cal_height = 210

box_l = cal_len/7
box_h = cal_height/7

def draw_box(l, h):
    for i in range(2):
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

def draw_month_box(l,h):             
    for i in range(2):
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

    
def draw_table():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range (6):
        for i in range(7):
            draw_box(box_l, box_h)
            turtle.penup()
            turtle.goto(turtle.xcor() + box_l, turtle.ycor())
            turtle.pendown()
        
        turtle.penup()
        turtle.goto(0, turtle.ycor() - box_h)
        turtle.pendown()

    turtle.penup()
    turtle.goto(0, box_h)
    turtle.pendown()
    draw_month_box(cal_len, box_h)


def calendar_of_2023(month):
    
    cal = calendar.monthcalendar(2023, month)
    month_name = calendar.month_name[month]

    days = ["Mo", "Tu","We", "Th","Fr", "Sa", "Su"]

    turtle.penup()
    turtle.goto(150,10)
    turtle.write(f"{month_name} 2023")                             # writing month name

    for i, u in enumerate (days):                                 
        turtle.goto(0 + (i *50) +25 ,-25)                   
        turtle.write(f"{u}")                                     # writng dates "Mo", "Su"

    for week in cal:
        for day in week:
            if day != 0:
                turtle.goto(0 + (week.index(day) * 50) +25, -30 -((cal.index(week)) * 30) -20)
                turtle.write(f"{day}")

    draw_table()
    

calendar_of_2023(6)
turtle.update()
turtle.done()

