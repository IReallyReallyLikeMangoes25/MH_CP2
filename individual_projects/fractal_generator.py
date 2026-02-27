# MH 1st fractal generator program
#x = 0
#y = 200

# import turtle
import turtle

# function to draw triangle, depth, color, base location, base side length, and base times to repeat
def draw_fractal(depth, color, x, y, side_length):
    turtle.up()
    turtle.goto(x, y)
    repeat = 3
    # draws three base triangles
    draw_triangles(side_length, color)
    # if the depth is 0 then exit the function
    if depth == 0:
        return
    # otherwise:
    else:
        # for loop that loops as many times as to repeat
        for triangle in range(repeat):
            # draws 3 triangles
            draw_triangles(side_length, color)
            # moves locations to the beginning of the next triangle
            turtle.fd(side_length)
        # sets new triangle side length
        # sets new beginning location
        # subtracts one from depth
        # multiplies times to repeat by three
        # runs the function again, passing through depth, color, new location, new side length, and times to repeat

# draw three triangles function, takes in side length and color:
def draw_triangles(side_length, color):
    turtle.color(color)
    turtle.right(60)
    # draws large triangle with 2X side length
    turtle.down()
    turtle.fd(side_length * 2)
    turtle.right(120)
    turtle.fd(side_length * 2)
    turtle.right(120)
    turtle.fd(side_length * 2)
    # draws smaller triangle inside with normal side length upsidown
    turtle.right(180)
    turtle.fd(side_length)
    turtle.left(120)
    turtle.fd(side_length)
    turtle.right(120)
    turtle.fd(side_length)
    turtle.right(120)
    turtle.fd(side_length)
    turtle.left(60)

# menu function
    # asks user the desired depth
    # asks user the desired color
    # runs generation function, passing through chosen depth and color

turtle.done()