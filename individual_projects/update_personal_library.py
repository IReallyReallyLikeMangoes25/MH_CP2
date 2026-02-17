# Mh first update personal library program

# add full display function
# add update function, takes in the collection dictionary
def update(rock_collection):
    # asks user 

# add load csv function
def load_csv():
    # loops over csv and converts lines into dictionaries
    with open("individual_projects/collection.csv", "r") as collection:
        content = csv.reader(collection)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
        return rows

# add save changes function that takes in the rock collection dictionary
def save_changes(rock_collection):
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.

# view function, takes in dictionary
def view_collection(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        # loops over dictionary, priting key value pairs one by one
        for key, value in rocks.items():
            print(f"{key}:{value}")

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
        to_remove = (input("What rock/mineral would you like to remove?\n"))
        while True:
            if to_remove not in rocks:
                to_remove = (input("That is not an option. What rock/mineral would you like to remove?\n"))
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
    in_collection = False
    # asks user what they want to search for (rock/mineral name or rock/mineral type)
    search = input("What would you like to search for:\n1. Rock/Mineral name\n2. Rock/Mineral type\n")
    while True:
        # if they want to search by name, ask them for the rock/mineral name
        if search == "1":
            name = input("What is the rock/mineral you are searching for?\n")
            # if it's in the dictionary print out it's key value pair
            for key, value in rocks.items():
                if key == name:
                    print(f"{key}, {value}")
                    in_collection = True
            # if it's not in the dictionary display that it is not in the dictionary
            if in_collection == False:
                print("That is not in your collection.")
            break
        # if they want to search for type, as them for a rock?mineral type
        elif search == "2":
            type_of_rock = input("What type of rock/mineral are you searching for?\n")
            # if it's in the dictionary print out it's key value pair
            for key, value in rocks.items():
                if value == type_of_rock:
                    print(f"{key}, {value}\n")
                    in_collection = True
            # if it's not in the dictionary display that it is not in the dictionary
            if in_collection == False:
                print("That is not in your collection.")
            break
        else:
            print("That is not an option.")
            search = input("What would you like to search for:\n1. Rock/Mineral name\n2. Rock/Mineral type")

# menu function
def menu():
    while True:
        # tuple containing strings that say the options of what to do
        options = ("1. View your collection","2. Add to your collection", "3. Remove from your collection", "4. Search your collection", "5. Exit")
        # print the tuple
        for i in options:
            print(i)

    # ask user what they would like to do from the given options
        choice = input("Which number would you like to do?\n")
    # if they want to view run the view function
        if choice == "1":
            view_collection(collection)
    # if they want to add run the add function
        elif choice == "2":
            new_name, new_type = add()
            collection[new_name] = new_type
            print("Added")
    # if they want to remove run the remove function
        elif choice == "3":
            delete = remove(collection)
            del collection[delete]
            print("Removed")
    # if they want to search run the search function
        elif choice == "4":
            search(collection)
        elif choice == "5":
            break
        else:
            continue

menu()
