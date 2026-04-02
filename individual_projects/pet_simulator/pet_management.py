# MH 1st pet management functions

from pet_class import pet
# NEEDS:
# Funtion to create pet
# Function to view list of pets
# Function to view specific stats for a pet
# Function to get rid of pet
# function to put away and choose new pet

# create pet function, takes in pet list:
def create_pet(pets, species):
    i = 1
    # asks new pets name
    name = input("\nWhat is your new pet's name going to be: ")
    # prints species options
    for animal in species:
        print(f"{i}. {animal}")
        i += 1
    # asks what species the pet is
    while True:
        species_choice = input("\nWhat species will your new pet be: ")
        if int(species_choice) > len(species):
            print("\nThat is not an option.")
            continue
        else: break
    species_choice = species[int(species_choice) - 1]
    name = pet(name, species_choice, 0, 0, 0, 0, 0, "active")
    name = name.convert_to_dict()
    pets.append(name)
    return pets


# view pet list function, takes in pet list:
def view_all(pets):
    i = 1
    # loops over the list of pets and prints each ones name, species, and age
    for pet in pets:
        print(f"{i}. {pet["name"]}: {pet["species"]}, age: {pet["age"]}")
        i += 1


# view pet stats function, takes in pet list:
def view_stats(pets):
    # finds that pet in the list and prints all it's stats besides status
    for pet in pets:
        if pet["status"] == "active":
            print(f"{pet["name"]} : {pet["species"]}\nAge: {pet["age"]}\nLevel: {pet["level"]}\nHunger: {pet["hunger"]}, Happiness: {pet["happiness"]}, Energy: {pet["energy"]}")
        else:
            continue

# abandon function, takes in pet list:
def abandon(pets):
    view_all(pets)
    # asks which pet to get rid of
    while True:
        choice = input("What pet would you like to get rid of (This is permanent!): ")
        if int(choice) > len(pets):
            continue
        else: 
            choice = pets[int(choice) - 1]
            break
    # finds that pet in the list and removes it
    for pet in pets:
        if pet == choice:
            print(f"{choice["name"]} has been removed.")
            pets.remove(pet)
    # returns updated list
    return pets


# select new pet function:
def select_new(pets, current):
    view_all(pets)
    # print list of pets and ask user which they would like to play with
    while True:
        choice = input("Which pet do you want to get out: ")
        if int(choice) > len(pets):
            continue
        else: 
            choice = pets[int(choice) - 1]
            break
    # set that pet's status to "active"
    for pet in pets:
        if pet["name"] == current:
            pet["status"] = "inactive"
        if pet["name"] == choice:
            pet["status"] = "active"
    current = choice
    return pets, current