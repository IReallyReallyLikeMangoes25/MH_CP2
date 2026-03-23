# MH 1st interaction functions
from pet_management import *
import random
# NEEDS:
# pet
# play
# feed
# sleep

# pet function:
def pet(name):
    silly_scenario = ["It seems happy but also suspicious... Be on guard.", "It says 'thank you' in perfect english.", "It takes a moment to ask itself why it listens to someone with such clammy hands.", "As thanks it bakes you a terrible smelling cake (the cake tastes suspiciously good though).", "In it's whirlwind of ecitement it grows a moustash that promptly falls off... It looks like you probably shouldn't worry."]
    print(f"You pet {name}... {silly_scenario(random.randint(1, 5))} + Happiness + energy")
    source = "hapiness/energy"
    # prints the interaction and returns + for happiness and energy
    return 5, 3, source

# play function:
def play(name, inventory)
    silly_scenario = ["the evil rat king came and tortured the neighbor.", "your mother in law called.", "a black hole sucked the nearby Seven Eleven into nothingness.", "the earthworms began to debate slug rights.", "Chet the bird-man trampled your tulips."]
    toys = []
    for i, item in inventory:
        if item["category"] = "toy":
            toys.append(item)
    for i, toy in toys:
        print(f"{i}. {toy}")
    while True:
        choice = input("Which toy would you like to play with: ")
        if choice.isalnum:
            choice = int(choice)
                if choice > len(toys):
                    continue
                else: break
        print(f"You and {name} played with {toys[choice]}. It was fun until {silly_scenario[random.randint(1, 5)]}")
        hapiness = toys["choice"]["use"]
        source = "hapiness/hunger/energy"
    # prints interaction and returns + for hapiness and - for hunger and - for energy
        return hapiness, 5, -5, source

# feed function:
def feed(name, inventory):
    silly_scenario = ["It yells at you almost exactly like Gordon Ramsey would.", "It eats and disapears for a moment, returning soon after with a gift... It's your boss's toupee.", "It eats the bowl... Food is food I guess.", "It tries to pick up a fork and knife and comes to the dissapointing realization that it has no thumbs.", "It rolls a die... The die lands on a six. It then winks at you and eats.", "You then sit there wondering why ever you would feed it that."]
    foods = []
    for i, item in inventory:
        if item["category"] = "food":
            foods.append(item)
    for i, food in foods:
        print(f"{i}. {food}")
    while True:
        choice = input(f"Which food are you going to feed {name}: ")
        if choice.isalnum:
            choice = int(choice)
                if choice > len(foods):
                    continue
                else: break
        print(f"You give {name} {food}. {silly_scenario[random.randint(1, 5)]} + Hapiness - Hunger + Energy")
        hapiness = toys["choice"]["use"]
        source = "hapiness/hunger/energy"
    # prints interaction and returns + for hapiness and - for hunger and + for energy
        return hapiness, -5, 5, source
    # prints interaction and returns - for hunger

# sleep function:
def sleep(name)
    silly_scenario = ["It rebels by sleeping in the fireplace and then blames you for the charcoal all over it.", "It promtly falls asleep where it stands (onto the send button of the angry email you weren't actually going to send to your boss).", "It decides the basement would be a nice place to sleep, but upon waking up it knocks through the salt barrier that was keeping the monster at bay.", "It is so resistant to the idea that you have to call in a professional pet hypnotizer.", "It looks at you in a way that says 'sleeping killed my mother, why would you do this?"]
    print(f"You make {name} take a nap... {silly_scenario[random.randint(1, 5)]} + Sleep")
    source = "sleep"
    # prints interaction and returns + for sleep
    return 5, source