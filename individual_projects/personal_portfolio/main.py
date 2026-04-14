# MH 1st main function
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from gui_management import *
from functools import partial

# main function:
def main():
        def library_info(elements, root):
                open_library(elements, root)
        def gen_info(elements, root):
                open_generator(elements, root)
        def gradebook_info(elements, root):
                open_gradebook(elements, root)
        def sim_info(elements, root):
                open_simulator(elements, root)
        root = tk.Tk()
        root.title("Set Budget Limits")
        root.columnconfigure(0, minsize = 50)
        root.minsize(300, 250)
        root.maxsize(500, 800)
        description = tk.Label(root, text = "Welcome to Mirai's Personal Portfolio project! Choose a project below to learn more about it!", wraplength = 200)
        learned = tk.Label(root, text = "What I Learned:\nNothing here yet!")
        challenges = tk.Label(root, text = "What Challenged Me:\nNothing here yet!", wraplength = 200)
        run_btn = tk.Button(root, text = "Select a project to run it.")
        elements = [description, learned, challenges, run_btn]
        library_btn = tk.Button(root, text = "Personal Library", command = partial(library_info, elements, root))
        generator_btn = tk.Button(root, text = "Fractal Generator", command = partial(gen_info, elements, root))
        gradebook_btn = tk.Button(root, text = "Simple Gradebook", command = partial(gradebook_info, elements, root))
        simulator_btn = tk.Button(root, text = "Pet Simulator", command = partial(sim_info, elements, root))
        # provides four project options: update personal library, fractal generator, simple gradebook, and pet simulator
        description.grid(row = 1, column = 1, columnspan = 3)
        learned.grid(row = 4, column = 1, columnspan = 3)
        challenges.grid(row = 5, column = 1, columnspan = 3)
        library_btn.grid(row = 2, column = 1, columnspan = 2)
        generator_btn.grid(row = 2, column = 3, columnspan = 2)
        gradebook_btn.grid(row = 3, column = 1, columnspan = 2)
        simulator_btn.grid(row = 3, column = 3, columnspan = 2)
        run_btn.grid(row = 6, column = 1, columnspan = 3)
        root.mainloop()

main()