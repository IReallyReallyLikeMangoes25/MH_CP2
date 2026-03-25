# MH 1st pet simulator main
from pet_management import *
from interactions import *
from csv_management import *
from pet_class import *
from pet_shop import *
from work import *
from time_management import *
from events import *
import random

species = ["Earth mouse", "North Noxian speiglehoof", "Common tentacle entity", "Urnoctan Gizard muncher", "Stair - creeping plastog", "Livnertian wallox"]

def main(species):
    actions = 0
    pets = load_pets()
    others = load_other()
    inventory = load_inventory()
    shop_items = load_shop()
    print(others)
    print("Welcome to Mirai's pet simulator program! In this little game you take care of awesome pets. When asked to choose between options, please put in a number given!")
    # if the user does not already have a pet make them create one
    if len(pets) == 0:
        print("Let's create your first pet!")
        pets = create_pet(pets, species)
        save_pets(pets)
    # if the user already has pets, present these options: choose pet, work, go to pet shop, view all pet, abandon pet, quit
    while True:
        for pet in pets:
                if pet["status"] == "active":
                    current = pet
                current["age"] = int(current["age"])
                current["happiness"] = int(current["happiness"])
                current["energy"] = int(current["energy"])
                current["hunger"] = int(current["hunger"])
                current["level"] = int(current["level"])
        num = random.randint(1,5)
        if num == 5:
            num = random.randint(1,5)
            if num == 1:
                happiness, energy = invasion(current["name"])
                current["happiness"] += happiness
                current["energy"] += energy
            elif num == 2:
                energy = local_crazy_crashout(current["name"])
                current["energy"] += energy
            elif num == 3:
                energy = rabies_dad(current["name"])
                current["energy"] += energy
            elif num == 4:
                happiness = lotion_release(current["name"])
                current["happiness"] += happiness
            elif num == 5:
                cash = bank_robbery(current["name"])
                others[1]["value"] += cash
                save_other(others)
        if actions == 3:
            actions = 0
            print("A day has elapsed.")
            others["day"] = update_time(others[2]["value"])
            pets = update_age(pets, others["day"])
        choice = input("What would you like to do:\n1. Choose pet\n2. Work\n3. Go to pet shop\n4. View all pets\n5. Abandon pet\n6. Create new pet\n7. Quit\n")

# for any given choice run the corresponding function
        if choice == "1":
            for pet in pets:
                if pet["status"] == "active":
                    current = pet
            current["age"] = int(current["age"])
            current["happiness"] = int(current["happiness"])
            current["energy"] = int(current["energy"])
            current["hunger"] = int(current["hunger"])
            current["level"] = int(current["level"])
            actions += 1
            pets, current = select_new(pets, current)
            # if the user chooses to get out a pet run the select pet function and present new options: choose work, pet, play, sleep, feed, view pet stats, go to pet shop, quit
            while True:
                if actions == 3:
                    actions = 0
                    others["day"] = int(others["day"])
                    print("A day has elapsed.")
                    others["day"] = update_time(others["value"])
                    pets = update_age(pets, ["day"])
                choice = input("What would you like to do:\n1. Pet\n2. Play\n3. Sleep\n4. Feed\n5. View status\n6. Go to pet shop\n7. Work\n8. Quit\n")
                if choice == "1":
                    actions += 1
                    happiness, energy = pet_animal(current["name"])
                    current["happiness"] += happiness
                    current["energy"] += energy
                    continue
                elif choice == "2":
                    actions += 1
                    happiness, hunger, energy = play(current["name"], inventory)
                    current["happiness"] += happiness
                    current["hunger"] += hunger
                    current["energy"] += energy
                    continue
                elif choice == "3":
                    actions == 1
                    energy = sleep(current["name"])
                    current["energy"] += energy
                    continue
                elif choice == "4":
                    actions += 1
                    happiness, hunger, energy, inventory = feed(current["name"], inventory)
                    current["happiness"] += happiness
                    current["hunger"] += hunger
                    current["energy"] += energy
                    save_inventory(inventory)
                    continue
                elif choice == "5":
                    actions += 1
                    view_stats(pets)
                elif choice == "6":
                    others["glorpcoin"] = int(others["glorpcoin"])
                    actions += 1
                    inventory, glorpcoin = pet_shop(shop_items, glorpcoin["glorpcoin"], inventory)
                    save_inventory(inventory)
                elif choice == "7":
                    others["glorpcoin"] = int(others["glorpcoin"])
                    actions += 1
                    print("Back to the grind at the good ol' 11/7 seven... Hey- here comes a customer now!")
                    glorpcoin = work(glorpcoin["value"], customers_list_format, customers)
                elif choice == "8":
                    break
                else:
                    print("That is not an option.")
                    continue
        elif choice == "2":
            others["glorpcoin"] = int(others["glorpcoin"])
            actions += 1
            glorpcoin = work(glorpcoin["value"], customers_list_format, customers)
        elif choice == "3":
            others["glorpcoin"] = int(others["glorpcoin"])
            actions += 1
            inventory, glorpcoin = pet_shop(shop_items, glorpcoin["value"], inventory)
            save_inventory(inventory)
        elif choice == "4":
            actions += 1
            view_all(pets)
        elif choice == "5":
            actions += 1
            pets = abandon(pets) 
            save_pets(pets)
        elif choice == "6":
            for pet in pets:
                if pet["status"] == "active":
                    pet["status"] = "inactive"
            pets = create_pet(pets, species)
            save_pets(pets)
        elif choice == "7":
            print("Thanks for playing!")
            break
        else:
            print("That is not an option, input again.")
            continue
    save_pets(pets)
    return others
    # if the user chooses to quit stop running the code

others = main(species)
save_other(others)

