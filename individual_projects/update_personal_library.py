# Mh first update personal library program
import csv
# add full display function, takes in collection dictionary
def full_display(rocks):
    if len(rocks) <= 0:
        print("There are no rocks or minerals in your collection.")
    else:
        num = 1
        # loops over dictionary printing every item and all its details
        for rock in rocks:
            print(f"{num}. Name : {rock["Name"]}, Category : {rock["Category"]}, Crystal System : {rock["Crystal System"]}, Formula : {rock["Formula"]}")
            num += 1

# add update function, takes in the collection dictionary
def update(rocks):
    # prints full list with numbers
    if len(rocks) <= 0:
        print("There are no rocks or minerals in your collection.")
    else:
        # loops over dictionary printing key value pairs one by one and a number for each pair
        full_display(rocks)
    # asks user which number they would like to edit
    while True:
        to_update = input("what number do you want to update?\n")
        if to_update.isnumeric() == False or int(to_update) > len(rocks):
            print("That input is not valid. Please make sure it is a number that was provided.")
            continue
        else:
            to_update = int(to_update)
            break
    # asks what part they want to edit
    while True:
        section = input("What part do you want to update? 1. Name, 2. Category, 3. Crystal System, or 4. Formula\n")
        if section == "1":
            section = "Name"
            break
        elif section == "2":
            section = "Category"
            break
        elif section == "3":
            section = "Crystal System"
            break
        elif section == "4":
            section = "Formula"
            break
        else:
            print("That is not an option.")
            continue
    # changes that part based off their input
    new = input("What would you like to change it to?\n")
    rocks[to_update-1][section] = new
    # reaturns updated dictionary
    return rocks

# add load csv function
def load_csv():
    # loops over csv and converts lines into dictionaries
    with open("individual_projects/collection.csv", "r") as collection:
        content = csv.reader(collection)
        row_count = sum(1 for row in content)
        collection.seek(0)
        if row_count == 0:
            headers = ["Name", "Category", "Crystal System", "Formula"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
        return rows

# add save changes function that takes in the rock collection dictionary
def save_changes(rocks):
    fieldnames = ["Name", "Category", "Crystal System", "Formula"]
    # loops over csv and dictionary changing every line of the csv to be the same as in the dictionary.
    with open("individual_projects/collection.csv", "w", newline = "") as collection:
        writer = csv.DictWriter(collection, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(rocks)

# view function, takes in dictionary
def simple_display(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        num = 1
        # loops over dictionary, priting key value pairs one by one
        for rock in rocks:
            print(f"{num}. Name : {rock["Name"]}, Category : {rock["Category"]}")
            num += 1


# remove function, takes in dictionary
def remove_choice(rocks):
    if len(rocks) <= 0:
        print("There are currently no rocks or minerals in your collection.")
    else:
        # loops over dictionary printing key value pairs one by one and a number for each pair
        full_display(rocks)
        # asks user what number they would like to remove
        while True:
            to_remove = (input("What rock/mineral would you like to remove?\n"))
            # removes that number if that is a valid choice, if not it asks again
            if to_remove.isnumeric() == False:
                print("Please input a number.")
                continue
            else:
                to_remove = int(to_remove)
                if to_remove > len(rocks):
                    print("Your collection does not contain that item.")
                    continue
                else:
                    rocks.pop(to_remove - 1)
                    break
    return rocks

# add function
def add():
    # asks user the name of the rock/mineral they would like to add
    name = input("What is the name of the rock/mineral you wish to add?\n")
    # asks user for the rocks/minerals category
    category = input("What category of rock/mineral is it?\n")
    # asks user for the rocks/minerals system
    system = input("What is the rock/minerals system?\n")
    # asks user for the rocks/minerals formula
    formula = input("What is the rock/minerals formula?\n")
    # returns rock, category, system, and formula
    return name, category, system, formula

# menu function
def menu():
    rock_collection = load_csv()
    while True:
        # asks what the user wants to do
        action = input("\nWhat do you want to do? 1. View simple list, 2. View detailed list, 3. Update an item on the list, 4. Remove something from the list, or 5. Add something to the list, 6. Exit\n")
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
            save_changes(rock_collection)
            continue
        # if they want to remove run the remove function
        elif action == "4":
            rock_collection = remove_choice(rock_collection)
            save_changes(rock_collection)
        # if they want to add run the add function
        elif action == "5":
            name, category, system, formula = add()
            rock_collection.append({"Name" : name, "Category" : category, "Crystal System" : system, "Formula" : formula})
            save_changes(rock_collection)
            continue
        # if they want to exit exit the code
        elif action == "6":
            break
        else:
            print("That is not an option.")
            continue

menu()