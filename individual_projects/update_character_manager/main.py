#Import other files for functions
from char_manager import create_character, edit_character, return_items
from character_search import char_search
from random_generator import *
from visualize_data import *
from csv_management import *
from statistic_analysis import *

# dictionary to contain all characters
    # FOR ALL CHARACTERS
    # race and class stored in tuple
    # skills stored a set
    # atributtes in nested dictionary
    # inventory in list

# tuple of races
    # tuple that contians all available races
race_options = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")

# tuple of classes
    # tuple containing all available classes
class_options = ("Black Mage", "Warrior", "Thief", "White Mage")

#Define main
def main(race_options, class_options):
    print("Welcome to the RPG Character Manager. You can create, edit, and search for characters here.")
    while True:
        characters = load_df()
        choice = input("What would you like to do?\n1. Create a new character\n2. Edit an already made character\n3. Search/filter characters\n4. Generate new character\n5. Analyze character stats\n6. Visualize character data\n7.Exit\n")
        if choice == '1':
            characters = create_character(characters, race_options, class_options)
            save_df(characters)
        elif choice == '2':
            characters = edit_character(characters)
            save_df(characters)
        elif choice == '3':  
            char_search(characters)
        elif choice == '4':
            generator = RandomGenerator({'race': None, 'class': None, 'level': 0, 'atributtes': {'MP': 0, 'HP': 0, 'Str': 0, 'Atk': 0, 'Def': 0, 'Mag': 0, 'Spr': 0, 'Acc': 0, 'Spd': 0, 'Evs': 0}, 'skills': {None, None}, 'inventory': {'weapon': [None], 'armor': [None], 'equipment one': [None], 'equipment two': [None], 'equipment three': [None], 'equipment four': [None]}, 'info': {'quest': None, 'backstory': None, 'description': None, 'trait 1': None, 'trait 2': None, 'trait 3': None}})
            items = return_items
            char_class = generator.gen_base_info
            generator.gen_backstory
            generator.gen_description
            generator.gen_inventory(items[char_class]["Armor"], items[char_class]["Weapons"], items["Equipment"], items["Two"], items["Three"])
            generator.gen_quest
            generator.gen_traits
            characters.append(generator)
            save_df(characters)

        elif choice == '5':
            while True:
                choice = input("How would you like to analyze your character data?\n1. View metrics across roster\n2. Comapre characters stats\n3. Quit\n")
                if choice == "1":
                    recents = []
                    for key, value in characters.items():
                        if "_" not in key:
                            recents.append(value)
                    analyzer = Statisticalanalyzer(recents)
                    analyzer.generate_report()

                elif choice == "2":
                    to_compare = []
                    while True:
                        amount = input("How many characters do you want to make a bar graph for: ")
                        if amount.isalnum == False or int(amount) > len(characters):
                            print("Please input a number, and make sure you have that many characters.")
                            continue
                        else:
                            break
                    amount = int(amount)
                    for i in range(amount):
                        character = char_search(characters)
                        to_compare.append(character)
                    analyzer = Statisticalanalyzer(to_compare)
                    analyzer.generate_report(to_compare)
                elif choice == "3":
                    break
                else:
                    continue
        elif choice == '6':
            to_graph = []
            while True:
                choice = input("How would you like to visualize data?\n1. Bar graph (current character stats)\n2. Radar chart (current character stats)\n3. Line chart (character stats over time)\n4. Exit visualization")
                if choice == '1':
                    while True:
                        amount = input("How many characters do you want to make a bar graph for: ")
                        if amount.isalnum == False or int(amount) > len(characters):
                            print("Please input a number, and make sure you have that many characters.")
                            continue
                        else:
                            break
                    amount = int(amount)
                    for i in range(amount):
                        character = char_search(characters)
                        to_graph.append(character)
                    char_visualize = DataVisualization(to_graph)
                    char_visualize.bar_graph()

                elif choice == '2':
                    while True:
                        amount = input("How many characters do you want to make a radar chart for: ")
                        if amount.isalnum == False or int(amount) > len(characters):
                            print("Please input a number, and make sure you have that many characters.")
                            continue
                        else:
                            break
                    amount = int(amount)
                    for i in range(amount):
                        character = char_search(characters)
                        to_graph.append(character)
                    char_visualize = DataVisualization(to_graph)
                    char_visualize.radar_graph()

                elif choice == '3':
                    character = char_search(characters)
                    while True:
                        stat = input("What stat do you want to see the prograssion of:\n1. Attack\n2. Defense\n3. Magic\n4. Speed\n5. Health").lower()
                        if stat == '1':
                            char_visualize = DataVisualization(characters)
                            char_visualize.line_chart(characters, "attack")
                        elif stat == '2':
                            char_visualize = DataVisualization(characters)
                            char_visualize.line_chart(characters, "defense")
                        elif stat == '3':
                            char_visualize = DataVisualization(characters)
                            char_visualize.line_chart(characters, "magic")
                        elif stat == '4':
                            char_visualize = DataVisualization(characters)
                            char_visualize.line_chart(characters, "speed")
                        elif stat == '5':
                            char_visualize = DataVisualization(characters)
                            char_visualize.line_chart(characters, "health")
                        else:
                            print("That is not an option provided. Please input a number given in the list.")

                elif choice == '4':
                    break
                else:
                    print("That is not an option.")
                    continue

        elif choice == '7':
            print("Thank you for using the updated RPG character manager program!")
            break

#define a function to return characters
def char_return(characters):
    return characters

#Run Main
main(race_options, class_options)