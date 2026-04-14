# MH 1st run project functions

from fractal_generator.fractal_gen_main import main as fractal_main
from personal_library.update_personal_library import menu
from pet_simulator.pet_sim_main import main as pet_main
from pet_simulator.pet_sim_main import species as pet_species
from simple_grade_book.gradebook_main import main as gradebook_main

import tkinter as tk

# run update personal library:
def run_library(root):
    # opens terminal widget for personal library and runs it
    def run():
        instruction = tk.Label(root, text = "Please look at the terminal now!")
        instruction.config(fg = "green")
        instruction.grid()
        menu()
        instruction.grid_forget()
        instruction.destroy()
    open_btn = tk.Button(root, text = "Run This Project", command = run)
    return open_btn
        

# run fractal generator:
def run_generator(root):
    # opens terminal widget for personal library and runs it
    def run():
        instruction = tk.Label(root, text = "Please look at the terminal now!")
        instruction.config(fg = "green")
        instruction.grid()
        fractal_main()
        instruction.grid_forget()
        instruction.destroy()
    open_btn = tk.Button(root, text = "Run This Project", command = run)
    return open_btn

# run simple gradebook:
def run_gradebook(root):
    # opens terminal widget for personal library and runs it
    def run():
        instruction = tk.Label(root, text = "Please look at the terminal now!")
        instruction.config(fg = "green")
        instruction.grid()
        gradebook_main()
        instruction.grid_forget()
        instruction.destroy()
    open_btn = tk.Button(root, text = "Run This Project", command = run)
    return open_btn

# run pet simulator:s
def run_simulator(root):
    # opens terminal widget for personal library and runs it
    def run():
        instruction = tk.Label(root, text = "Please look at the terminal now!")
        instruction.config(fg = "green")
        instruction.grid()
        pet_main(pet_species)
        instruction.grid_forget()
        instruction.destroy()
    open_btn = tk.Button(root, text = "Run This Project", command = run)
    return open_btn
