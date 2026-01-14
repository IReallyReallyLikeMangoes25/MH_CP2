# MH 1st personal library project

# dictionary for all rocks/minerals
collection = {}

# view function, takes in dictionary
def view_collection(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        # loops over dictionary, priting key value pairs one by one
        for i in rocks:
            print(i)

# remove function, takes in dictionary
def remove(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        num = 1
        # loops over dictionary printing key value pairs one by one and a number for each pair
        for i in rocks:
            print(num, i)
            num += 1
        # asks user what number they would like to remove
        to_remove = int(input("What number would you like to remove?\n"))
        while True:
            if to_remove > len(rocks):
                print("That is not an option.")
                to_remove = int(input("What number would you like to remove?\n"))
            else:
                break
        # rerurns that number
    return to_remove

# add function
def add():
    # asks user the name of the rock/mineral they would like to add
    name = input("What is the name of the rock/mineral you wish to add?\n")
    # asks user for the rocks/minerals type
    type = input("What type of rock/mineral is it?\n")
    # returns rock and type
    return name, type

# search function, takes in dictionary
def search(rocks):
    # asks user what they want to search for (rock/mineral name or rock/mineral type)
    search = input("What would you like to search for:\n1. Rock/Mineral name\n2. Rock/Mineral type")
    while True:
        # if they want to search by name, ask them for the rock/mineral name
        if search == "1":
            name = input("What is the rock/mineral you are searching for?\n")
            # if it's in the dictionary print out it's key value pair
            if name in rocks:
                print(rocks(name))
            # if it's not in the dictionary display that it is not in the dictionary
            else:
                print("That is not in your collection.")
            break
        # if they want to search for type, as them for a rock?mineral type
        elif search == "2":
            type = input("What type of rock/mineral are you searching for?\n")
            # if it's in the dictionary print out it's key value pair
            for i in rocks:
                pass
            # if it's not in the dictionary display that it is not in the dictionary
            break
        else:
            print("That is not an option.")
            search = input("What would you like to search for:\n1. Rock/Mineral name\n2. Rock/Mineral type")

# menu function
    # tuple containing strings that say the options of what to do
    # print the tuple
    # ask user what they would like to do from the given options
    # if they want to view run the view function
    # if they want to add run the add function
    # if they want to remove run the remove function
    # if they want to search run the search function
