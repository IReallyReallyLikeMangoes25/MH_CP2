# MH 1st financial calculator project

# asks user what they want to do (goal, interest, budget, discount, tip)
choice = input("What do you want to do?\n1. Save to a goal\n2. Calculate interest\n3. Allocate a budget\n3. Calculate a discount\n4. Calculate a tip")

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
    interest = print(f"At the end of {months} you will have {compound(current_amount, months, rate)} money in your bank account.")
    return interest

# function for budget allocator:
def budget_allocator():
    # asks user how much money they will be budgeting
    amount = input("How much money will you be budgeting?")
    # asks what percentage they will allocate to savings
    savings = input("What percentage will be allocated to savings?")
    # asks what percentage they will allocate to home
    home = input("Wat percentage will be allocated to your home?")
    # asks what percentage will be allocated to entertainment
    # asks what percentage will be allocated to food
    # adds up the percentages to make sure it's not over 100%
    # if it's over 100% ask user questions again
    # if it's not:
    # take savings percentage out of total
    # take home percentage out of total
    # take entertainment percentage out of total
    # take food percentage out of total
    # return how much they can spend on everything

# function for discount calculator:
    # asks how much the item originally was
    # asks what percentage the discount is
    # take discount percentage out of original value
    # returns discounted value

# function for tip calculator:
    # asks how much they spent
    # asks how much they would like to tip (5, 10, 15, 20)
    # takes the tip percentage out of how much they spent
    # return tip value

# loop that runs until they quit
    # if the user goal run the goal function
    # if the user says interest run the interest function
    # if the user wants to budget run the budget function
    # if the user wants to discount use the discount funciton
    # if the user wants to tip run the tip function
    # ask the user if they want to do soething else or quit