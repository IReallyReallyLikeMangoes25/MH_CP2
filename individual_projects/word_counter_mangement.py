# MH 1st word counter management file

from pathlib import Path
from time_file import *

# word count function:
def count_words(relative_path):
    words = 0
    # loops over the file counting every word
    with open(relative_path, "r") as file:
        content = file.readlines()
        for line in content:
            if "Updated : " not in line and "Word count : " not in line and line != "\n":
                line = line.split()
                words += len(line)
    # returns the amount of words
    return words

# get file function:
def get_file():
    while True:
        # asks user for the exact relative path of the file they want to update (must be txt)
        file = input("Please input the exact relative path of the file you would like to open (must be txt):\n")
        # checks if it's a txt file
        file_path = Path(file)
        file_type = file_path.suffix
        # if it's not ask again
        if file_type != ".txt":
            print("That is not a txt file.")
            continue
        # if it is continue
        else: break
    # returns relative path
    return file_path

# update file function:
def update_file(words, relative_path):
    # asks user what they want to add to the file
    to_add = input("\nType below what you would like to add:\n")
    with open(relative_path, "a") as file:
        file.write(f"\n\n{to_add}")
    # uses save time function to get the time updated
    time_updated = save_time()
    # runs word count function
    words = count_words(relative_path)
    # adds new text to the file
    # adds time updated and word count
    with open(relative_path, "a") as file:
        file.write(f"\n\nWord count : {words}\nUpdated : {time_updated}")
    # returns word count, time updated, and what they added for use later
    return time_updated, words

# view file function:
def view_file(words, relative_path):
    # opens the file and prints it, if it's empty it prints it is empty
    with open(relative_path, "r") as file:
        if int(words) == 0:
            print("\nThis file is empty.")
        else:
            content = file.read()
            print(content)