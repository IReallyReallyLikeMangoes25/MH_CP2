# MH 1st generate triangles file

# draw three triangles function, takes in side length and color:
def draw_triangle(side_length, color, turtle):
    turtle.seth(0)
    turtle.right(60)
    turtle.color(color)
    # draws a triangle
    turtle.fd(side_length)
    turtle.right(120)
    turtle.fd(side_length)
    turtle.right(120)
    turtle.fd(side_length)
    turtle.right(120)
