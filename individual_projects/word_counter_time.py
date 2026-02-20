# MH second word counter time page

# import time
import time

# save time function:
def save_time():
    # gets current time
    current_time = time.time()
    # converts time to be readeable
    readable_time = time.ctime(current_time)
    # returns a string with the time
    return str(readable_time)