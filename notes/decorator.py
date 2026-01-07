# MH 1st, decorator function example
def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator
def greet():
    print("Hey hey")

greet()