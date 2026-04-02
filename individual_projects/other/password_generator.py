# MH 1st pasword generator project

# import random
import random

# list for all letters A-Z
uppercase = ["A", 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "v", "W", "X", "Y", "Z"]
# list for all letters a-z
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# list for special characters
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "=", "?", "<", ">"]
# list for numbers
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# generation function, takes in prefferences and the lists:
def generate(password_length, upper_list, lower_list, special_list, nums_list, use_capitals, use_lowercase, use_numbers, use_specials):
    passwords = ["", "", "", ""]
    # loop that runs four times
    for password in range(4):
        # loop that runs until password is preffered length
        for item in range(password_length):
            # generate random number 1-4
            add = random.randint(1, 4)
            # if the number is one add a random uppercase letter
            if add == 1:
                passwords[password] += upper_list[random.randint(0, 25)]
            # if the number is two add a random number
            if add == 2:
                passwords[password] += nums_list[random.randint(0, 8)]
            # if the number is three add a random special character
            if add == 3:
                passwords[password] += special_list[random.randint(0, 12)]
            # if the number is four add a random lowercase letter
            if add == 4:
                passwords[password] += lower_list[random.randint(0, 25)]
        # if capitals shouldn't be used:
        if use_capitals == "n":
            # password loop function run for capitals
            passwords[password] = remove(upper_list, lower_list, nums_list, special_list, passwords[password])
        # if lowercase shouldn't be used:
        if use_lowercase == "n":
            # password loop function run for lowercase
            passwords[password] = remove(lower_list, upper_list, nums_list, special_list, passwords[password])
        # if numbers shouldn't be used:
        if use_numbers == "n":
            # password loop function run for numbers
            passwords[password] = remove(nums_list, lower_list, upper_list, special_list, passwords[password])
        # if special characters shouln't be used:
        if use_specials == "n":
            # password function run for special characters
            passwords[password] = remove(special_list, lower_list, nums_list, upper_list, passwords[password])
        # save fixed password
        print(passwords[password])

# function that loops through the password to change certain items, takes in a condition to change by and the lists:
def remove(condition, keep_1, keep_2, keep_3, incomplete_password):
    incomplete_password = list(incomplete_password)
    # loop going over the password:
    for char in incomplete_password:
        # if this item in the password contains the condition:
        if char in condition:
            # generate random number 1-3 to choose a list (cannot be the list they said not to use)
            add = random.randint(1, 3)
            # changes the item to another randomly generated character
            if add == 1:
                incomplete_password[incomplete_password.index(char)] = keep_1[random.randint(0, len(keep_1) - 1)]
            if add == 2:
                incomplete_password[incomplete_password.index(char)] = keep_2[random.randint(0, len(keep_2) - 1)]
            if add == 3:
                incomplete_password[incomplete_password.index(char)] = keep_3[random.randint(0, len(keep_3) - 1)]
    incomplete_password = "".join(incomplete_password)
    return incomplete_password

# main function:
def main():
    # loop that runs until they want to exit
    while True:
        good_choices = False
    # ask if they would like to generate passwords
        what_to_do = input("What would you like to do:\n1. Generate Paswords\n2. Exit\n")
    # if they do:
        if what_to_do == "1":
            while True:
                # ask user preffered length
                length = input("How long should the password be?\n")
                if length.isdigit == False:
                    continue
                else:
                    int_length = int(length)
                    break
            while good_choices == False:
                choices = []
                # ask user if capitals should be used
                capitals_prefference = input("Should capital letters be used? (Y/N)\n").strip().lower()
                choices.append(capitals_prefference)
                # ask user if lowercase should be used
                lowercase_prefference = input("Should lowercase letters be used? (Y/N)\n").strip().lower()
                choices.append(lowercase_prefference)
                # ask user if special characters should be used
                special_prefference = input("Should special characters be used? (Y/N)\n").strip().lower()
                choices.append(special_prefference)
                # ask user if numbers should be used
                numbers_prefference = input("Should numbers be used? (Y/N)\n").strip().lower()
                choices.append(numbers_prefference)
                for i in choices:
                    if i != "y" or "n":
                        good_choices = True
        # run generation function on their prefferences and print results
            if capitals_prefference and lowercase_prefference and special_prefference and numbers_prefference == "n":
                print("If you don't actually want to generate a password then exit.")
                continue
            else:
                generate(int_length, uppercase, lowercase, special_characters, numbers, capitals_prefference, lowercase_prefference, numbers_prefference, special_prefference)
        if what_to_do == "2":
            break
        else:
            continue

main()