# MH 1st financial calculator project

# asks user what they want to do (goal, interest, budget, discount, tip)
choice = input("What do you want to do?\n1. Save to a goal\n2. Calculate interest\n3. Allocate a budget\n4. Calculate a discount\n5. Calculate a tip\n6. Quit")

# function for saving to a goal:
def save_to_goal():
    # asks what amount they are saving to
    goal = float(input("What is your goal?\n"))
    # asks how much they make weekly
    weekly = float(input("How much do you make weekly?\n"))
    #  divides how much they are saving to by how much they make
    weeks = f"It will take you {goal/weekly} weeks to save to your goal."
    # return how many weeks it will take
    return weeks


# function for compound interest calculator:
def calcualte_interest():
    # asks how much is currently in their bank account
    current_amount = float(input("How much is in your bank account?"))
    # asks how many months they want to calculate for
    months = float(input("How many months would you like to calculate for?"))
    # asks their interest rate
    rate = float(input("What is your interest rate?"))
        # function inside that takes in how much money they have, how many months, and their interest rate:
    def compound(current_amount, months, rate):
            # loops over how much money is in their account forevery month
            for i in range(months):
            # takes interest rate % out of current money
            # adds it to current money
                current_amount += (current_amount/rate) * 100
        # return what they will have
            return current_amount
    # returns calculation function
    interest = f"At the end of {months} you will have {compound(current_amount, months, rate)} money in your bank account."
    return interest

# function for budget allocator:
def budget_allocator():
    while True:
    # asks user how much money they will be budgeting
        amount = float(input("How much money will you be budgeting?"))
        # asks what percentage they will allocate to savings
        savings = float(input("What percentage will be allocated to savings?"))
        # asks what percentage they will allocate to home
        home = float(input("Wat percentage will be allocated to your home?"))
        # asks what percentage will be allocated to entertainment
        entertainment = float(input("What percentage will be allocated to entertainment?"))
        # asks what percentage will be allocated to food
        food = float(input("What percentage will be allocated for food?"))
        # adds up the percentages to make sure it's not over 100%
        # if it's over 100% ask user questions again
            if (food + entertainment + home + savings + amount) <= 100:
                break
    # if it's not:
    # take savings percentage out of total
    savings =  (amount/savings) * 100
    # take home percentage out of total
    home = (amount/home) * 100
    # take entertainment percentage out of total
    entertainment = (amount/entertainment) * 100
    # take food percentage out of total
    food = (amount/food) * 100

    budget  = f"Savings: {savings}\nHome: {home}\nEntertainment: {entertainment}\nFood: {food}"
    # return how much they can spend on everything
    return budget

# function for discount calculator:
def discount_calculator():
    # asks how much the item originally was
    og_price = float(input("How much was the item originally?"))
    # asks what percentage the discount is
    discount = float(input("What percentage is the discount?"))
    # take discount percentage out of original value
    discounted = f"The discounted price is {og_price - ((og_price/discount) * 100)}"
    # returns discounted value
    return discounted

# function for tip calculator:
def tip_calculator():
    # asks how much they spent
    spent = float(input("How much did you spend?"))
    # asks how much they would like to tip
    percentage = float(input("What percentage would you like to tip?"))
    # takes the tip percentage out of how much they spent
    tip = f"You need to tip {(spent/percentage) * 100}"
    # return tip value
    return tip

# loop that runs until they quit
while True:
    # if the user goal run the goal function
    if choice == "1":
        print(save_to_goal())
    # if the user says interest run the interest function
    elif choice == "2":
        print(calcualte_interest())
    # if the user wants to budget run the budget function
    elif choice == "3":
        print(budget_allocator())
    # if the user wants to discount use the discount funciton
    elif choice == "4":
        print(discount_calculator())
    # if the user wants to tip run the tip function
    elif choice == "5":
        print(tip_calculator())
    elif choice == "6":
        break
    else:
        choice = input("What do you want to do?\n1. Save to a goal\n2. Calculate interest\n3. Allocate a budget\n4. Calculate a discount\n5. Calculate a tip\n6. Quit")
        continue
