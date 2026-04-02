# mh first pet class file

class pet:
    def __init__(instance, name, species, age, level, hunger, happiness, energy, status):
        instance.name = name
        instance.species = species
        instance.age = age
        instance.level = level
        instance.hunger = hunger
        instance.happiness = happiness
        instance.energy = energy
        instance.status = status
    
    def convert_to_dict(self):
        return {"name" : self.name, "species" : self.species, "age" : self.age, "level" : self.level, "hunger" : self.hunger, "happiness" : self.happiness, "energy" : self.energy, "status" : self.status}