# Mh 1st csv management functions

# NEEDS:
# function to save to inventory csv
# function to load inventory csv
# function to load shop items csv
# functions to load/save pet csv
# functions to load/save other csv

import csv
# save to inventory csv function, takes in inventory:
def save_inventory(inventory):
    fieldnames = ["name", "price", "use", "category"]
    # updates whole csv with inventory
    with open("pet_simulator/inventory.csv", "w", newline = "") as inventory_csv:
        writer = csv.DictWriter(inventory_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(inventory)


# load inventory csv function:
def load_inventory():
    # opens and saves csv as a list
    with open("pet_simulator/inventory.csv", "r") as inventory_csv:
        content = csv.reader(inventory_csv)
        row_count = sum(1 for row in content)
        inventory_csv.seek(0)
        if row_count == 0:
            headers = ["name", "price", "use", "category"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
    # returns inventory list
            return rows

# load shop items csv function:
def load_shop():
     # opens and saves csv as a list
    with open("pet_simulator/shop_items.csv", "r") as inventory_csv:
        content = csv.reader(inventory_csv)
        row_count = sum(1 for row in content)
        inventory_csv.seek(0)
        if row_count == 0:
            headers = ["name", "price", "use", "category"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
    # returns inventory list
            return rows

# save to pet csv function, takes in pets:
def save_pets(pets):
    fieldnames = ["name", "species", "age", "level", "hunger", "happiness", "energy", "status"]
    # updates whole csv with inventory
    with open("pet_simulator/pets.csv", "w", newline = "") as pet_csv:
        writer = csv.DictWriter(pet_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(pets)


# load pet csv function:
def load_pets():
    # opens and saves csv as a list
    with open("pet_simulator/pets.csv", "r") as pet_csv:
        content = csv.reader(pet_csv)
        row_count = sum(1 for row in content)
        pet_csv.seek(0)
        if row_count == 0:
            headers = ["name", "species", "age", "level", "hunger", "happiness", "energy", "status"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3], headers[4] : line[4], headers[5] : line[5], headers[6] : line[6], headers[7] : line[7]})
    # returns pet list
        return rows

def load_other():
    # opens and saves csv as a list
    with open("pet_simulator/other.csv", "r") as other_csv:
        content = csv.reader(other_csv)
        row_count = sum(1 for row in content)
        other_csv.seek(0)
        if row_count == 0:
            headers = ["name", "value"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1]})
    # returns other list
        return rows
    
def save_other(others):
    fieldnames = ["name", "value"]
    # updates whole csv with inventory
    with open("pet_simulator/other.csv", "w", newline = "") as other_csv:
        writer = csv.DictWriter(other_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(others)