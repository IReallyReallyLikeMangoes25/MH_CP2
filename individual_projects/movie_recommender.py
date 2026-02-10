# MH 2nd Movie recommender project
import csv
import math
with open("individual_projects/Movies list.py", mode = "r") as movie_list
# function to load csv file:
def load_csv(movies):
    movies = csv.reader(movies)
    headers = next(movies)
    rows = []
    for line in movies:
        rows.append({headers[0] : line[0], headers[1] : line[1], headers[3] : line[3], headers[4] : line[4], headers[5] : line[5], headers[6], line[6]})
    return rows

# function for searching for genre:
def search_genre(movies):
    movies_with_genre = []
    # ask user what genre they are looking for
    desired_genre = input("What genre are you searching for?").strip().lower().title()
    # loop through the genre section of the file and if any movies are that genre save them inside a list in this function
    for movie in movies:
        if desired_genre in movie["Genre"]:
            movies_with_genre.append(movie)
    # return the list of movies with that genre
    return movies_with_genre

# function for searching for director:
def search_director(movies)
    movies_by_director = []
    # ask user what director they are looking for
    director = input("What director are you searching for?").lower().strip().title()
    # loop through the director section of the file and if any movies were made by that director add them to a list inside this function
    for movie in movies:
        if director in movie["Director"]:
            movies_by_director.append[movie]
    # return the list of all movies with that director
    return movies_by_director

# function for searching for actors:
def search_actors(movies):
    movies_with_actors = []
    # ask user how many actors they will be searching for
    how_many = input("How Many actord are you searching for?")
    how_many = int(how_many)
    # ask for the names of how ever many actors they are searching for
    for num in range(how_many):
        actor = input(f"What is actor {num}s name?")
    # loop through the file and if any movie has any of those actors save it to a list in this function
        for movie in movies:
            if actor in movie["Actors"]:
                movies_with_actors.append(movie)
    # return the list of movies with selected actors
    return movies_with_actor

# function for searching for length:
def search_length(movies):
    ideal_length_movies = []
    minimum = 0
    maximum = math.inf
    # ask if they want to search for minimum, maximum, or both
    choice = input("What do you want to search for?\n1.Minimum\n2. Maximum\n3. Both")
    # if they say minimum ask for the minimum length and set maximum to infinite
    if choice == "1":
        minimum = input("What is the minimum desired length?")
        minimum = int(minimum)
    # if they say maximum ask for maximum length and set minimum to 0
    elif choice == "2":
        maximum = inout("What is the maximum desired length")
        maximum = int(maximum)
    # if they say both ask for both
    elif choice == "3":
        minimum = input("What is the minimum desired length?")
        minimum = int(minimum)
        maximum = inout("What is the maximum desired length")
        maximum = int(maximum)
    else:
        print("That isn't an option")
    for movie in movies:
        if movie["Length"] >= minimum and movie["Length"] <= maximum:
            ideal_length_movies.append(movie)
    # loop through the file and if a movie has a length somewhere inbetween the max and min
    # if it does add it to a list of movies inside of this function
    # return the list of movies
    return ideal_length_movies

# function for searching using selected filters, takes in what filters they chose:
def search_with_filters(filter_one, filter_two, movies):
    # if they chose to search for genre run the search for genre function
    if filter_one or filter_two == "1":
        search_genre(movies)
    # if they chose to search for director run the the search for director function
    # if they chose to search for actors run the search for actors function
    # if they chose to search for lenght run the search for length function
    # take the two lists that were returned by two of the functions and loop over both, seeing if any movies are in both
    # if a movie is in both add it to a new list inside this function
    # return the list of movies

# print search results function, takes in list of movies:
    def search_results(movies):
    # loops over list printing movies one by one
        for movie in movies:
            print(movie).replace("["," ").replace("]"," ")

# print full list function, takes in full list:
    def print_all(movies)
    # loops over list printing movies one by one
    for movie in movies:
        print(movie).replace("["," ").replace("]"," ")

# menu function:
    # ask is user wants to print the full list, search, or exit
    # if they want to print the full list run the print full list function
    # if they want to search print search options
    # ask if they will be searching for one or two filters
    # if they choose one ask for it then run the corresponding search function and print the resuts with the print searvch results function
    # if they want to search for two ask user for both and run the search using selected filters function and print the results with the print search results function
    # if they want to exit, exit the code
    # if their input is invalid ask again
