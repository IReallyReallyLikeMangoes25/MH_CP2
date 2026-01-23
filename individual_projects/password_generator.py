# MH 1st pasword generator project

# import random
import random

# list for all letters A-Z
uppercase = ["A", 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "v", "W", "X", "Y", "Z"]
# list for all letters a-z
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# list for special characters
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "=", "?", "<", ">"]

# prefferences function:
def prefferences():
    # ask user preffered length
    length = int(input("How long does your password need to be?\n"))
    # ask if capital letters should be used
    capitals = input("Should it contain capitals? (Y/N)\n").lower()
    # ask if lowercase letters should be used
    lowers = input("Should lowercase letters be used? (Y/N)\n").lower()
    # ask if numbers should be used
    nums = input("Should numbers be used? (Y/N)\n").lower()
    # ask if special characters should be used
    special_chars = input("Should special characters be used? (Y/N)\n").lower()
    # return all prefferences
    return length, capitals, lowers, nums, special_chars

# generation function, takes in prefferences and the lists:
def generate(password_length, upper_list, lower_list, special_list, use_capitals, use_lowercase, use_numbers, use_specials):
    passwords = ["", "", "", ""]

    # loop that runs four times
    for password in range(4):
        # loop that runs until password is preffered length
        for item in range(password_length):
            # generate random number 1-4
            list = random.randint(1, 4)
            # if the number is one add a random uppercase letter
            if list == 1:
                passwords[password.extend(upper_list[random.randint(0, 26)])]
            # if the number is two add a random number
            if list == 2:
                passwords[password.extend(number_list[random.randint(0, 9)])]
            # if the number is three add a random special character
            if list == 3:
                passwords[password.extend(special_list[random.randint])]
            # if the number is four add a random lowercase letter
            if list == 4:
                passwords[password.extend(lower_list[random.randint])]
        # if capitals shouldn't be used:
            # password loop function run for capitals
        # if lowercase shouldn't be used:
            # password loop function run for lowercase
        # if numbers shouldn't be used:
            # password loop function run for numbers
        # if special characters shouln't be used:
            # password function run for special characters
        # save fixed password

# function that loops through the password to change certain items, takes in a condition to change by and the lists:
def check(condition, keep_1, leep_2, keep_3, incomplete_password):
    # loop going over the password:
    for item in incomplete_password:
        # if this item in the password contains the condition:
        if item in condition:
            # generate random number 1-3 to choose a list (cannot be the list they said not to use)
            list = random.randint(1-3)
            # changes the item to another randomly generated character
            if list == 1:
                item = keep_1[random.randint]

# main function:
    # loop that runs until they want to exit
    # ask if they would like to generate passwords
    # if they do:
    # run prefferences function
    # run generation function on their prefferences and print results

