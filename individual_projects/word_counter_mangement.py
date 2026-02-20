# MH second word counter file update page

# import from other files
from word_counter_time import *

# runs word count function

# update file function:
def update_file(words):
    # asks user what they want to add to the file
    to_add = input("\nType below hat you would like to add:\n")
    with open("individual_projects/word_counter_file.txt", "a") as file:
        file.write(to_add)
    to_add = to_add.split()
    # uses save time function to get the time updated
    time_updated = save_time()
    # runs word count function
    words += count_words(len(to_add))
    # adds new text to the file
    # adds time updated and word count
    with open("individual_projects/word_counter_file.txt", "a") as file:
        file.write(f"\n\nUpdated : {time_updated}\nWord count : {words}")
    # returns word count, time updated, and what they added for use later
    return time_updated, words

# view file function:
def view_file(words):
    # opens the file and prints it, if it's empty it prints it is empty
    with open("individual_projects/word_counter_file.txt", "r") as file:
        if int(words) == 0:
            print("\nThis file is empty.")
        else:
            content = file.read()
            print(content)

# word count function:
def count_words(added):
    # loops over what was added to the file separating words at spaces and counting how many there are
    added = added.split()
    count = len(added)
    # returns the amoutn of words
    return str(count)