# MH 1st position tracking/setting file

# position functions, take in side length and move turtle to beginning position of next triangle
def position_1_draw(side_length, turtle):
    turtle.penup()
    turtle.fd(side_length)
    turtle.pendown()
def position_2_draw(side_length, turtle):
    turtle.penup()
    turtle.right(120)
    turtle.fd(side_length)
    turtle.pendown()
def final_position_draw(side_length, turtle):
    turtle.penup()
    turtle.fd(side_length)
    turtle.left(60)
    turtle.fd(side_length)
    turtle.pendown()

def position_2_recurse(side_length, turtle):
    turtle.penup()
    turtle.right(180)
    turtle.fd(side_length)
    turtle.right(60)
    turtle.fd(side_length)
    turtle.pendown()
def final_position_recurse(side_length, turtle):
    turtle.penup()
    turtle.seth(0)
    turtle.fd(side_length)
    turtle.pendown()
