# MH 1st personal portfolio gui functions pseudocode
import tkinter as tk
from personal_portfolio.run_projects import *

# open update personal library info:
def open_library(elements, root):
    # hides anything about other projects that was onscreen
    elements[0].destroy()
    elements[1].destroy()
    elements[2].destroy()
    elements[3].destroy()
    # displays what the program is, what I learned, and challenges I overcame
    description = tk.Label(root, text = "My Personal Library project is for cataloging and organizing a rock collection. It allows you to save, delete, and edit rocks in your collection to keep track of them.", wraplength = 200)
    learned = tk.Label(root, text = "What I Learned:\n- How to use the CSV library\n- How to save and load data across runs")
    challenges = tk.Label(root, text = "What Challenged Me:\n- I had never worked with CSVs before, so it was difficult converting the data into a structure I was used to working with", wraplength = 200)
    # sets up run button
    open_btn = run_library(root)
    description.grid(row = 1, column = 1, columnspan = 3)
    learned.grid(row = 4, column = 1, columnspan = 3)
    challenges.grid(row = 5, column = 1, columnspan = 3)
    open_btn.grid(row = 6, column = 1, columnspan = 3)
    elements[0] = description
    elements[1] = learned
    elements[2] = challenges
    elements[3] = open_btn


# open fractal generator info:
def open_generator(elements, root):
    # hides anything about other projects that was onscreen
    elements[0].destroy()
    elements[1].destroy()
    elements[2].destroy()
    elements[3].destroy()
    # displays what the program is, what I learned, and challenges I overcame
    description = tk.Label(root, text = "My Fractal Generator project is for generating a Sierpinski triangle. it allows you to choose the color and depth of the fractal.", wraplength = 200)
    learned = tk.Label(root, text = "What I Learned:\n- How to implement recursive functions\n- How to reason backwards through problems that require recursive thinking", wraplength = 200)
    challenges = tk.Label(root, text = "What Challenged Me:\n- Keeping track of the turtles position and knowing how far it should move while drawing the triangle was very difficult to think through", wraplength = 200)
    # sets up run button
    open_btn = run_generator(root)
    description.grid(row = 1, column = 1, columnspan = 3)
    learned.grid(row = 4, column = 1, columnspan = 3)
    challenges.grid(row = 5, column = 1, columnspan = 3)
    open_btn.grid(row = 6, column = 1, columnspan = 3)
    elements[0] = description
    elements[1] = learned
    elements[2] = challenges
    elements[3] = open_btn

# open simple gradebook info:
def open_gradebook(elements, root):
    # hides anything about other projects that was onscreen
    elements[0].destroy()
    elements[1].destroy()
    elements[2].destroy()
    elements[3].destroy()
    # displays what the program is, what I learned, and challenges I overcame
    description = tk.Label(root, text = "My Simple Gradebook project is for managing a group of students and their grades. It allows you to register student year, and grades for all their classes, and has the capability to calculate student and class average grade.", wraplength = 200)
    learned = tk.Label(root, text = "What I Learned:\n- How to implement classes that work with each other\n- How to organize data between classes", wraplength = 200)
    challenges = tk.Label(root, text = "What Challenged Me:\n- It was difficult to figure out what exaclty each class needed to do, and how they would interact with each other", wraplength = 200)
    # sets up run button
    open_btn = run_gradebook(root)
    description.grid(row = 1, column = 1, columnspan = 3)
    learned.grid(row = 4, column = 1, columnspan = 3)
    challenges.grid(row = 5, column = 1, columnspan = 3)
    open_btn.grid(row = 6, column = 1, columnspan = 3)
    elements[0] = description
    elements[1] = learned
    elements[2] = challenges
    elements[3] = open_btn

# open pet simulator info:
def open_simulator(elements, root):
    # hides anything about other projects that was onscreen
    elements[0].destroy()
    elements[1].destroy()
    elements[2].destroy()
    elements[3].destroy()
    # displays what the program is, what I learned, and challenges I overcame
    description = tk.Label(root, text = "My Pet Simulator project is a simulation game where you own and take care of alien pets. It currently has the capablities to create new pets and interact with them, though it is a little choppy.", wraplength = 170)
    learned = tk.Label(root, text = "What I Learned:\n- How classes work and how to implement them in a program\n- How to save data from a class to a CSV and load data from a CSV to an object", wraplength = 170)
    challenges = tk.Label(root, text = "What challenged Me:\n- It was a really large project, and I really struggled with thinking of methods to perform functions quickly and writing them in good time", wraplength = 170)
    # sets up run button
    open_btn = run_simulator(root)
    description.grid(row = 1, column = 1, columnspan = 3)
    learned.grid(row = 4, column = 1, columnspan = 3)
    challenges.grid(row = 5, column = 1, columnspan = 3)
    open_btn.grid(row = 6, column = 1, columnspan = 3)
    elements[0] = description
    elements[1] = learned
    elements[2] = challenges
    elements[3] = open_btn