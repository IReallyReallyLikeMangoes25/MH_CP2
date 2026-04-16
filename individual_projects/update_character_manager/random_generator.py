from faker import Faker

class RandomGenerator:
    def __init__(self, character):
        self.character = character
    
    # generate backstory:
    def gen_backstory(self):
        # list of locations
        locations = ["the Ancient Forest", "the City in the Clouds", "the City Under the Mountain", "the Kingdom of Faeries", "the Land of Dragons", "the Isle of Wind", "the Kingdom of Shadows", "the Village Between the Seas", "the Elven City of Light", "the Castle of the great Mage of Fire"]
        # list of events
        events = ["there was a terrible fire", "a dragon attacked", "a great flood destroyed it all", "a witch cursed the place", "an earthquake shook it to the ground", "a giant stommped it to dust", "a great war fell upon the land", "the dead rose from their graves", "a tyrant king conquered it", "the troll queen claimed it as her own"]
        # randomizes new name
        name = Faker.name()
        # randomly selects from the list of locations and list of events and plugs the character name into them
        backstory = f"{name} hails from {Faker.random_element(locations)}. They lived peacefully until {Faker.random_element(events)}, and they had to leave their home."
        # updates character backstory and name
        self["backstory"] = backstory
        self["name"] = name
    
    def gen_base_info(self):
        races = ["Human", "Dragonborn", "Halfling", "Elf", "Ogre", "Dwarf", "Tiefling"]
        classes = ["Black Mage", "Warrior", "Thief", "White Mage"]
        self["race"] = Faker.random_element(races)
        self["class"] = Faker.random_element(classes)
        return self["class"]

    def to_dict(self):
        char = {
        "race" : (self["race"]),
        "class" : (self["class"]),
        "level" : 0,
        "atributtes" : {
            "MP" : 0,
            "HP" : 0,
            "Str" : 0,
            "Atk" : 0,
            "Def" : 0,
            "Mag" : 0,
            "Spr" : 0,
            "Acc" : 0,
            "Spd" : 0,
            "Evs" : 0
        },
        "skills" : {"None yet", "None yet"},
        "inventory" : {
            "weapon" : [self["weapon"]],
            "armor" : [self["robes"]],
            "equipment one" : [self["item 1"]],
            "equipment two" : [self["item 2"]],
            "equipment three" : [self["item 3"]],
            "equipment four" : [self["item 4"]]
        },
        "info" : {
            "quest" : self["quest"],
            "backstory" : self["backstory"],
            "description" : self["description"],
            "trait 1" : self["trait 1"],
            "trait 2" : self["trait 2"], 
            "trait 3" : self["trait 3"]
        }
    }

        return self["name"], char 
    # generate character traits:
    def gen_traits(self):
        # list of character traits
        character_traits = ["Kind", "Honest", "Brave", "Trustworthy", "Reliable", "Compassionate", "Empathetic", "Optimistic", "Generous", "Confident", "Selfish", "Jealous", "Rude", "Dishonest", "Disloyal", "Amoral", "Obnoxious", "Lazy", "Self-Centered", "Arrogant"]
        one = Faker.random_element(character_traits)
        character_traits.remove(one)
        two = Faker.random_element(character_traits)
        character_traits.remove(two)
        three = Faker.random_element(character_traits)
        character_traits.remove(three)
        self["trait 1"] = one
        self["trait 2"] = two
        self["trait 3"] = three

    # generate description:
    def gen_description(self):
        # uses faker to get random facets of the characters appearance
        height = ["tall", "average height", "short"]
        eyes = Faker.color_name()
        hair = Faker.color_name()
        age = Faker.numerify( "##" )
        self["description"] = f"They are {Faker.random_element(height)} with {hair} hair, {eyes} eyes, and are {age} years old."

    # generate inventory, takes in available items:
    def gen_inventory(self, armors, weapons, other, other_2, other_3):
        armor = Faker.random_element(armors)
        weapon = Faker.random_element(weapons)
        item_1 = Faker.random_element(other)
        item_2 = Faker.random_element(other_2)
        item_3 = Faker.random_element(other_3)
        item_4 = Faker.random_element(other)
        # takes random items from each section of the available items and returns them
        self["weapon"] = weapon
        self["armor"] = armor
        self["item 1"] = item_1
        self["item 2"] = item_2
        self["item 3"] = item_3
        self["item 4"] = item_4

    # generate quest:
    def gen_quest(self):
        # list of bosses
        bosses = ["Dragon King, Snaggletooth ", "Dark Mage Alzphar", "Orc Queen, Yvaine Skullcrusher", "Elves of the Darkwood", ""]
        # list of magical artifacts
        artifacts = ["the Truth Hammer", "the Compass of Health", "the Wind Shell", "the Diadem of Flames", "the Protection Amulet", "the Salve of Intelligence", "the Pendant of Light", "the Pickaxe of Darkness", "the Hail Spyglass", "the Amulet of Rage"]
        # list of lairs
        lairs = ["the Sluggish Stream", "the Sheltered Valley", "the Graveyard of Kings", "the Pool of Reflection", "the Corpse Tree", "the Waterfall of Fire", "the Hollow of Dreams", "the Watchtower of Gods", "the Meadow of Peace", "the Scortched Temple"]
        # takes a random index from each list and creates a quest
        self["quest"] = f"Their quest is to defeat {Faker.random_element(bosses)} so that they may retrieve {Faker.random_element(artifacts)} from {Faker.random_element(lairs)}"