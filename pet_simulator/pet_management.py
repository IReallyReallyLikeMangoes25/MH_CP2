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
    species_choice = input("\nPlease input the number corresponding to the species you choose: ")
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
    choice = input("what pet would you like to see the stats of: ")
    # finds that pet in the list and prints all it's stats besides status
    for pet in pets:
        if pet["name"] == choice:
            print(f"{pet.name} : {pet.species}\nAge: {pet.age}\nLevel: {pet.level}\nHunger: {pet.hunger}, Happiness: {pet.happiness}, Energy: {pet.energy}")
        else:
            continue

# abandon function, takes in pet list:
def abandon(pets):
    view_all(pets)
    # asks which pet to get rid of
    while True:
        choice = input("Which pet do you want to get rid of (This is permanent!): ")
        if choice not in pets:
            continue
        else: break
    # finds that pet in the list and removes it
    pets.pop(choice)
    print("/n Pet Removed")
    # returns updated list
    return pets

# select new pet function:
def select_pet(pets):
    # print list of pets and ask user which they would like to play with
    view_all(pets)
    # set that pet's status to "active"