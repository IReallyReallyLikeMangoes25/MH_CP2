# MH 1st financial calculator project

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
def calculate_interest():
    # asks how much is currently in their bank account
    current_amount = float(input("How much is in your bank account?\n"))
    # asks how many months they want to calculate for
    years = float(input("How many years would you like to calculate for?\n"))
    # asks their interest rate
    rate = float(input("What is your interest rate?\n"))
        # function inside that takes in how much money they have, how many months, and their interest rate:
    def compound(amount, amount_of_years, interest_rate):
            total = amount * (1 + (interest_rate/100)) ** amount_of_years
        # return what they will have
            return total
    # returns calculation function
    money = compound(current_amount, years, rate)
    interest = f"At the end of {years} years you will have {money} in your bank account."
    return interest

# function for budget allocator:
def budget_allocator():
    while True:
    # asks user how much money they will be budgeting
        amount = float(input("How much money will you be budgeting?\n"))
        # asks what percentage they will allocate to savings
        savings = float(input("What percentage will be allocated to savings?\n"))
        # asks what percentage they will allocate to home
        home = float(input("What percentage will be allocated to your home?\n"))
        # asks what percentage will be allocated to entertainment
        entertainment = float(input("What percentage will be allocated to entertainment?\n"))
        # asks what percentage will be allocated to food
        food = float(input("What percentage will be allocated for food?\n"))
        # adds up the percentages to make sure it's not over 100%
        # if it's over 100% ask user questions again
        if (food + entertainment + home + savings + amount) >= 10:
            break
    # if it's not:
    # take savings percentage out of total
    savings =  (savings/100) * amount
    # take home percentage out of total
    home = (home/100) * amount
    # take entertainment percentage out of total
    entertainment = (entertainment/100) * amount
    # take food percentage out of total
    food = (food/100) * amount

    budget  = f"Savings: {savings}\nHome: {home}\nEntertainment: {entertainment}\nFood: {food}"
    # return how much they can spend on everything
    return budget

# function for discount calculator:
def discount_calculator():
    # asks how much the item originally was
    og_price = float(input("How much was the item originally?\n"))
    # asks what percentage the discount is
    discount = float(input("What percentage is the discount?\n"))
    # take discount percentage out of original value
    discounted = f"The discounted price is {og_price - ((discount/100) * og_price)}"
    # returns discounted value
    return discounted

# function for tip calculator:
def tip_calculator():
    # asks how much they spent
    spent = float(input("How much did you spend?\n"))
    # asks how much they would like to tip
    percentage = float(input("What percentage would you like to tip?\n"))
    # takes the tip percentage out of how much they spent
    tip = f"You need to tip {(percentage/100) * spent}"
    # return tip value
    return tip

# loop that runs until they quit
print("Hello! Welcome to Mirai's financial calculator, some instructions you should know are a sfollows:\n1. When asked for a percentage please input it without the percentage symbol\n2. If asked for an amount of something please only put the amount and not a name")
while True:
    choice = input("What do you want to do?\n1. Save to a goal\n2. Calculate interest\n3. Allocate a budget\n4. Calculate a discount\n5. Calculate a tip\n6. Quit\n")
    # if the user goal run the goal function
    if choice == "1":
        print(save_to_goal())
    # if the user says interest run the interest function
    elif choice == "2":
        print(calculate_interest())
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
        choice = input("What do you want to do?\n1. Save to a goal\n2. Calculate interest\n3. Allocate a budget\n4. Calculate a discount\n5. Calculate a tip\n6. Quit\n")
        continue