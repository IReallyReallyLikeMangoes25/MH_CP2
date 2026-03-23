 # MH 2nd work functions

# NEEDS:
# simple game to award in-game money
import random

# dictionary of customers, with their questions and the right answers
customers = {
    "name1" = {
        "question" : "",
        "responses" : {1, 2, 3, 4}
    },
    "name2" = {
        "question" : "",
        "responses" : {1, 2, 3, 4}
    }
}

def work(money, customer_list):
    earnings = 0
    # random customer appears from the customer dictionary and asks their question
    customer = customer_list(random.randint(1, 10))
    customer_list.pop(customer)
    print(customer["question"])
    # response option are given to the user
    for i, response in customer["responses"]:
        print(f"{i}. {response}")
    while True:
        pass
    # if the users response is the first saved answer add + 10 to earnings
    # if the users response is the second saved answer add + 5 to earnings
    # if the users response is the wrong answer then subtract - 10 from earnings
    # returns the days earnings