# MH 1st pet management functions


# NEEDS:
# pet class
# Funtion to create pet
# Function to view list of pets
# Function to view specific stats for a pet
# Function to get rid of pet
# function to put away and choose new pet


class pet:
    def initialize(instance, name, species, age, level, hunger, happiness, energy, status):
        instance.name = name
        instance.species = species
        instance.age = age
        instance.level = level
        instance.hunger = hunger
        instance.happiness = happiness
        instance.energy = energy
        instance.status = status


# create pet function, takes in pet list:
def create_pet(pets, species):
    # asks new pets name
    name = input("\nWhat is your new pet's name going to be?")
    # prints species options
    for i, animal in species:
        print(f"{i}. {animal}")
    # asks what species the pet is
    while True:
        species_choice = input("\nPlease input the number corresponding to the species you choose: ")
        if int(species_choice) > len(species) or int(species_choice) < len(species):
            print("\nThat is not an option.")
            continue
        else: break
    species_choice = species(int(species_choice))
    name = pet(name, species_choice, 0, 0, 0, 0, "active")
    pets.append(name)
    return pets


# view pet list function, takes in pet list:
def view_all(pets):
    # loops over the list of pets and prints each ones name, species, and age
    for i, pet in pets:
        print(f"{i}. {pet.name}: {pet.species}, {pet.age}")


# view pet stats function, takes in pet list:
def view_stats(pets):
    view_all(pets)
    # asks which pet they would lke to view
    while True:
        choice = input("what pet would you like to see the stats of: ")
        if choice not in pets:
            continue
        else: break
    # finds that pet in the list and prints all it's stats besides status
    for pet in pets:
        if pet.name == choice:
            print(f"{pet.name} : {pet.species}\nAge: {pet.age}\nLevel: {pet.level}\nHunger: {pet.hunger}, Happiness: {pet.happiness}, Energy: {pet.energy}")
        else:
            continue


# abandon function, takes in pet list:
def abandon(pets):
    view_all(pets)
    # asks which pet to get rid of
    while True:
        choice = input("What pet would you like to get rid of (This is permanent!): ")
        if choice not in pets:
            continue
        else: break
    # finds that pet in the list and removes it
    for pet in pets:
        if pet.name == choice:
            print(f"{choice} has been removed.")
            pets.pop(pet)
    # returns updated list
    return pets


# select new pet function:
def select_new(pets, current):
    view_all(pets)
    # print list of pets and ask user which they would like to play with
    while True:
        choice = input("Which pet do you want to get out: ")
        if choice not in pets:
            continue
        else: break
    # set that pet's status to "active"
    for pet in pets:
        if pet.name == current:
            pet.status = "inactive"
        if pet.name == choice:
            pet.status = "active"
    current = choice
    return pets, current


def save_inventory(inventory):
    fieldnames = ["name", "price", "use", "category"]
    with open("pet_simulator/inventory.csv", "w", newline = "") as inventory_csv:
    # updates whole csv with inventory
        writer = csv.DictWriter(inventory_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(inventory)


# load inventory csv function:
def load_inventory():
    # opens and saves csv as a list
    with open("pet_simulator/inventory.csv", "r") as inventory_csv:
        content = csv.reader(inventory.csv)
        row_count = sum(1 for row in content)
        collection.seek(0)
        if row_count == 0:
            headers = ["name", "price", "use", "category"]
        else:
            headers = next(inventory_csv)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
    # returns inventory list
    return rows


# load shop items csv function:
def load_shop():
    # opens and saves csv as a list
    with open("pet_simulator/shop_items.csv", "r") as shop_items:
        content = csv.reader(inventory.csv)
        row_count = sum(1 for row in content)
        collection.seek(0)
        if row_count == 0:
            headers = ["item", "price", "use", "category"]
        else:
            headers = next(shop_items)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
    # returns shop list
    return rows
