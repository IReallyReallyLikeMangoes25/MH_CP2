# mh 1st class relationships notes

class Vehicle:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")


# inheritance = is a 
# aggregation = has a

class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    
    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)

    def view_catalog(self):
        for i in self.catalog:
            print(i)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Title : {self.title} by {self.author}"
    
lib = Library("Provo Library")

lib.add_book(Book("Mostly Harmless", "Douglas Adams"))
lib.add_book(Book("The Once and Future King", "T.H. White"))
lib.add_book(Book("Scott Pilgrim's Finest Hour", "Bryan Lee O'Malley"))

lib.view_catalog()