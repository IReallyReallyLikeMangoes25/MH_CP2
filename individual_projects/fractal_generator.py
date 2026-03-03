# MH 1st fractal generation file

from positions import *
from draw_triangle import *

# function to draw fractal, takes in depth, color, and side length
def draw_fractal(color, side_length, current_level, desired_level, turtle):
    # if the level is not the smallest level, go a level inward and check again by calling this function
    if current_level < desired_level:
        draw_fractal(color, side_length/2, current_level+1, desired_level, turtle)
        # draw more triangles
        draw_fractal(color, side_length/2, current_level+1, desired_level, turtle)
        # go to next position
        position_2_recurse(side_length, turtle)
        # draw more triangles
        draw_fractal(color, side_length/2, current_level+1, desired_level, turtle)
        # go to next position
        final_position_recurse(side_length, turtle)
    # if the level is the smallest level draw many of the smallest triangle needed
    else:
        # actually draw the triangles now that you are in the smallest level
        draw_triangle(side_length, color, turtle)
        # go to next position
        position_1_draw(side_length, turtle)
        draw_triangle(side_length, color, turtle)
        # go to next position
        position_2_draw(side_length, turtle)
        draw_triangle(side_length, color, turtle)
        # go to next position
        final_position_draw(side_length, turtle)
