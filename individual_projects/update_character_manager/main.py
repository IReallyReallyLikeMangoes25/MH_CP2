#Import other files for functions
from char_manager import create_character, edit_character
from character_search import char_search
from random_generator import *
from visualize_data import *
from csv_management import *
from statistic_analysis import *

# dictionary to contain all characters
characters = {
    # FOR ALL CHARACTERS
    # race and class stored in tuple
    # skills stored a set
    # atributtes in nested dictionary
    # inventory in list
    "example_char" : {
        "race" : ("Dragonborn"),
        "class" : ("White Mage"),
        "level" : 10,
        "atributtes" : {
            "MP" : 1,
            "HP" : 2,
            "Str" : 3,
            "Atk" : 4,
            "Def" : 5,
            "Mag" : 6,
            "Spr" : 7,
            "Acc" : 8,
            "Spd" : 9,
            "Evs" : 10
        },
        "skills" : {"Cure", "Esuna"},
        "inventory" : {
            "weapon" : ["Wand"],
            "armor" : ["Robes"],
            "equipment one" : ["Classic Italian Pizza"],
            "equipment two" : ["Pot of Petunias"],
            "equipment three" : ["Bowling Pin"],
            "equipment four" : ["Sticky Hand"]
        },
        "info" : {
            "quest" : "none",
            "backstory" : "none",
            "description" : "none",
            "trait 1" : "none",
            "trait 2" : "none", 
            "trait 3" : "none"
        }
    }
}


# tuple of races
    # tuple that contians all available races
race_options = ("Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling")

# tuple of classes
    # tuple containing all available classes
class_options = ("Black Mage", "Warrior", "Thief", "White Mage")

#Define main
def main():
    print("Welcome to the RPG Character Manager. You can create, edit, and search for characters here.")
    while True:
        characters = load_csv()
        choice = input("What would you like to do?\n1. Create a new character\n2. Edit an already made character\n3. Search/filter characters\n4. Generate new character\n5. Analyze character stats\n6. Visualize character data\n7.Exit\n")
        if choice == '1':
            characters = create_character(characters, race_options, class_options)
            save_csv(characters)
        elif choice == '2':
            characters = edit_character(characters)
            save_csv(characters)
        elif choice == '3':  
            char_search(characters)
        elif choice == '4':
            generator = RandomGenerator({"name" : None, "race" : None, "class" : None, "level" : None, "attack" : None, "defense" : None, "magic" : None, "speed" : None, "health" : None, "item slot 1" : None, "item slot 2" : None, "item slot 3" : None, "item slot 4" : None, "weapon" : None, "armor" : None, "backstory" : None, "quest" : None, "description" : None, "trait 1" : None, "trait 2" : None, "trait" : None})
            generator.gen_backstory
            generator.gen_description
            generator.gen_inventory
            generator.gen_quest
            generator.gen_traits
            characters.append(generator)
            save_csv(characters)

        elif choice == '5':
            while True:
                choice = input("How would you like to analyze your character data?\n1. View metrics across roster\n2. Comapre characters stats\n")
                if choice == "1":
                    analyzer = Statisticalanalyzer(characters)
                    analyzer.generate_report

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
                    for i in amount:
                        character = char_search(characters)
                        to_compare.append(character)
                    analyzer = Statisticalanalyzer(to_compare)
                    analyzer.generate_report
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
                    for i in amount:
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
                    for i in amount:
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
main()