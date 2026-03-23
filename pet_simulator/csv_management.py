# Mh 1st csv management functions

# NEEDS:
# function to save to inventory csv
# function to load inventory csv
# function to load shop items csv

import csv
# save to inventory csv function, takes in inventory:
def save_inventory(inventory):
    fieldnames = ["name", "price", "use", "category"]
    # updates whole csv with inventory
    with open("pet_simulator/inventory.csv", "w", newline = "") as inventory_csv:
        writer = csv.DictWriter(inventory_csv, fieldnames = fieldnames)
        writer.writeheader()
        writer.wrtierows(inventory)


# load inventory csv function:
def load_inventory():
    # opens and saves csv as a list
    with open("pet_simulator/inventory.csv", "r") as inventory_csv:
        content = csv.reader(inventory_csv)
        row_count = sum(1 for row in content)
        content.seek(0)
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
        content.seek(0)
        if row_count == 0:
            headers = ["name", "price", "use", "category"]
        else:
            headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3]})
    # returns inventory list
            return rows