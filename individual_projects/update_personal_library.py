# Mh first update personal library program

# add full display function, takes in collection dictionary
def full_display(rocks):
    if len(rocks) <= 0:
        print("There are no rocks or minerals in your collection.")
    else:
        # loops over dictionary printing every item and all its details
        for key, value in rocks.items():
            print(f"{key[0]} : {value[0]}, {key[1]} : {value[1]}, {key[2]} : {value[2]}, {key[3]} : {value[3]}")

# add update function, takes in the collection dictionary
def update(rocks):
    # prints full list with numbers
     if len(rocks) <= 0:
        print("There are no rocks or minerals in your collection.")
    else:
        # loops over dictionary printing every item and all its details
        for i, key, value in rocks.items():
            print(f"{i}.{key[0]} : {value[0]}, {key[1]} : {value[1]}, {key[2]} : {value[2]}, {key[3]} : {value[3]}")
    # asks user which number they would like to edit
    to_update = input("what number do you want to update?\n") 
    to_update = int(to_update)
    # asks what part they want to edit
    section = input("What part do you want to update? 1. Name, 2. Category, 3. Crystal System, or 4. Formula\n")
    section = int(section)
    # changes that part based off their input
    new = input("What would you like to change it to?\n")
    rocks[to_update[section]] = new
    # reaturns updated dictionary
    return rocks

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
def save_changes(rocks):
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.
    with open("individual_projects/collection.csv", "w") as collection:
        writer = csv.writer(collection)
        writer.writeRows(rocks)

# view function, takes in dictionary
def simple_display(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        # loops over dictionary, priting key value pairs one by one
        for key, value in rocks.items():
            print(f"{key[0]}:{value[0]}, {key[1]}, {value[1]}")

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

# menu function
def menu():
    while True:
        rock_collection = load_csv()
        save_changes(rock_collection)
        # asks what the user wants to do
        action = input("What do you want to do? 1. View simple list, 2. View detailed list, 3. Update an item on the list, 4. Remove something from the list, or 5. Add something to the list, 6. Exit\n")
        # if they want to view the simple version run the simple view function
        if action == "1": 
            simple_display(rock_collection)
            continue
        # if they want to view the full version run the full view function
        elif action == "2":
            full_display(rock_collection)
            continue
        # if they want to update something run the update function
        elif action == "3":
            rock_collection = update(rock_collection)
            continue
        # if they want to add run the add function
        elif action == "4":
            rock_collection = add(rock_collection)
            continue
        # if they want to remove run the remove function
        elif action == "5":
            rock_collection = remove(rock_collection)
        # if they want to exit exit the code