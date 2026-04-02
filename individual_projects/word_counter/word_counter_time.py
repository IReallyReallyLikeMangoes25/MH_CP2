# MH 1st time handling page

import time

# save time function:
def save_time():
    # gets current time
    current_time = time.time()
    # converts time to be readeable
    readable_time = time.ctime(current_time)
    # returns a string with the time
    return str(readable_time)

# function to get last updated:
def update_time(relative_path):
    last_line = ""
    # loops over the file and finds the last line
    with open(relative_path, "r") as file:
    # if the line says when it was updated return the line
        for line in file:
            last_line = line
        if "Updated : " not in last_line:
        # if not return that the file has not yet been updated using this program
            return "This file has not yet been updated using this program."
        else:
            last_line = last_line.replace("Updated : ", "")
            return last_line