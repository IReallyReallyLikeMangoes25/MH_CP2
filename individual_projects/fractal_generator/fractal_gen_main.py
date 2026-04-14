# MH first fractal generator main file
from fractal_generator.fractal_gen import draw_fractal
import turtle

# menu function
def main():
    colors = ["red", "blue", "orange", "green", "yellow", "purple", "pink"]
    desired_depth = " "
    desired_color = " "
    print("Hello, welcome to Mirai's super awesome fractal generator. It generates a fractal (sierpinski triangle). You can choose the color and depth.\n")
    while desired_depth.isnumeric() == False:
        # asks user the desired depth
        desired_depth = input("What depth would you like the fractal to be?\n")
    desired_depth = int(desired_depth)
    while desired_color not in colors:
        # asks user the desired color
        desired_color = input("What color would you like it to be? (Red, orange, yellow, green, blue, purple, pink)\n").strip().lower()
    # runs generation function, passing through chosen depth and color
    fractal_window = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.goto(0, 200)
    t.pendown()
    rootwindow = fractal_window.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    t.speed(25)
    t.shape("turtle")
    draw_fractal(desired_color, 200, 1, desired_depth, t)

#main()
#turtle.done()
