# Mh 1st pet shop functions

# NEEDS:
# purchase/sell functions

# purchase function, takes in shop_items list:
def purchase(shop_items, money, inventory):
    # prints all items
    for i, item in shop_items:
        print(f"{i}. {item}, {item["price"]}")
    # asks player what they want to purchase
    while True:
        choice = input("Which item would you like to purchase: ")
        if int(choice) > len(shop_items):
            continue
        else:
            choice = shop_items[choice]
            break
    # adds item to inventory and subtacts the money
    inventory.append(choice)
    money -= choice["price"]
    # returns the updated inventory and money
    return inventory, money


# sell function, takes in inventory:
def sell(inventory, money):
    # prints out inventory
    for i, item in inventory:
        print(f"{i}. {item}")
    # asks what they want to sell
    while True:
        choice = input("Which item would you like to sell: ")
        if int(choice) > len(inventory):
            continue
        else:
            choice = inventory[choice]
            break
    # goes into inventory list and remove the item
    inventory.pop(choice)
    money += choice["price"]
    # return how much it was sold for and the updated inventory
    return inventory, money