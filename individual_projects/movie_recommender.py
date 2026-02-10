# MH 2nd Movie recommender project
import csv
import math
# function to load csv file:
def load_csv():
    with open("test.py/Movies list.csv", "r",) as movies:
        content = csv.reader(movies)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0] : line[0], headers[1] : line[1], headers[2] : line[2], headers[3] : line[3], headers[4] : int(line[4]), headers[5] : line[5]})
        return rows

load_csv()
# function for searching for genre:
def search_genre(movies):
    movies_with_genre = []
    # ask user what genre they are looking for
    desired_genre = input("What genre are you searching for?\n").strip().lower().title()
    # loop through the genre section of the file and if any movies are that genre save them inside a list in this function
    for movie in movies:
        if desired_genre in movie["Genre"]:
            movies_with_genre.append(movie)
    # return the list of movies with that genre
    if len(movies_with_genre) == 0:
        movies_with_genre = "There are no movies with this genre in the list."
    return movies_with_genre

# function for searching for director:
def search_director(movies):
    movies_by_director = []
    # ask user what director they are looking for
    director = input("What director are you searching for?\n").lower().strip().title()
    # loop through the director section of the file and if any movies were made by that director add them to a list inside this function
    for movie in movies:
        if director in movie["Director"]:
            movies_by_director.append(movie)
    # return the list of all movies with that director
    if len(movies_by_director) == 0:
        movies_by_director = "There are no movies with this Director in the list."
    return movies_by_director

# function for searching for actors:
def search_actors(movies):
    while True:
        movies_with_actors = []
        # ask user how many actors they will be searching for
        how_many = input("How Many actors are you searching for?\n")
        if how_many.isdigit() == False:
            continue
        else:
            how_many = int(how_many)
            break
    # ask for the names of how ever many actors they are searching for
    for num in range(how_many):
        actor = input(f"What is actor {num + 1}s name?\n")
    # loop through the file and if any movie has any of those actors save it to a list in this function
        for movie in movies:
            if actor in movie["Notable Actors"]:
                movies_with_actors.append(movie)
    # return the list of movies with selected actors
    if len(movies_with_actors) == 0:
        movies_with_actors = "There are no movies with these actors in the list."
    return movies_with_actors

# function for searching for length:
def search_length(movies):
    ideal_length_movies = []
    minimum = 0
    maximum = math.inf
    # ask if they want to search for minimum, maximum, or both
    choice = input("What do you want to search for?\n1.Minimum\n2. Maximum\n3. Both\n")
    # if they say minimum ask for the minimum length and set maximum to infinite
    if choice == "1":
        minimum = input("What is the minimum desired length?\n")
        minimum = int(minimum)
    # if they say maximum ask for maximum length and set minimum to 0
    elif choice == "2":
        maximum = input("What is the maximum desired length?\n")
        maximum = int(maximum)
    # if they say both ask for both
    elif choice == "3":
        minimum = input("What is the minimum desired length?\n")
        minimum = int(minimum)
        maximum = input("What is the maximum desired length\n")
        maximum = int(maximum)
    else:
        print("That isn't an option")
    for movie in movies:
        if movie["Length (min)"] >= minimum and movie["Length (min)"] <= maximum:
            ideal_length_movies.append(movie)
    # loop through the file and if a movie has a length somewhere inbetween the max and min
    # if it does add it to a list of movies inside of this function
    # return the list of movies
    if len(ideal_length_movies) == 0:
        ideal_length_movies = "There are no movies in this length  in the list."
    return ideal_length_movies

# function for searching using selected filters, takes in what filters they chose:
def search_with_filters(filter_one, filter_two, movies):
    filter_actors = movies
    filter_director = movies
    filter_genre = movies
    filter_length = movies
    two_filter_movies = movies
    # if they chose to search for genre run the search for genre function
    if filter_one or filter_two == "1":
        filter_genre = search_genre(movies)
    # if they chose to search for director run the the search for director function
    if filter_one or filter_two == "2":
        filter_director = search_director(movies)
    # if they chose to search for actors run the search for actors function
    if filter_one or filter_two == "3":
        filter_actors = search_actors(movies)
    # if they chose to search for lenght run the search for length function
    if filter_one or filter_two == "4":
        filter_length = search_length(movies)
    # take the two lists that were returned by two of the functions and loop over both, seeing if any movies are in both
    for movie in filter_actors:
        if movie in filter_director or filter_genre or filter_length:
    # if a movie is in both add it to a new list inside this function
            two_filter_movies.append(movie)
    # return the list of movies
    return two_filter_movies

# print search results function, takes in list of movies:
def search_results(movies):
        if isinstance(movies, str):
            print(movies)
        else:
        # loops over list printing movies one by one
            for movie in movies:
                print(movie)

# print full list function, takes in full list:
def print_all(movies):
    # loops over list printing movies one by one
    for movie in movies:
        print(f"{movie}")

# menu function:
def menu(movies):
    while True:
        # ask is user wants to print the full list, search, or exit
        what_to_do = input("What do you want to do?\n1. Print full list\n2. Search\n3. Exit\n")
        # if they want to print the full list run the print full list function
        if what_to_do == "1":
            print_all(movies)
        # if they want to search print search options
        elif what_to_do == "2":
            # ask if they will be searching for one or two filters
            filter_amount = input("How many filters would you like to apply (1/2)\n")
        # if they choose one ask for it then run the corresponding search function and print the resuts with the print searvch results function
            if filter_amount == "1":
                chosen_filter = input("What filter would you like to apply?\n1. Genre\n2. Director\n3. Actors\n4. Length\n")
                if chosen_filter == "1":
                    search_results(search_genre(movies))
                if chosen_filter == "2":
                    search_results(search_director(movies))
                if chosen_filter == "3":
                    search_results(search_actors(movies))
                if chosen_filter == "4":
                    search_results(search_length(movies))
        # if they want to search for two ask user for both and run the search using selected filters function and print the results with the print search results function
            if filter_amount == "2":
                chosen_filter_one = input("What filter would you like to apply?\n1. Genre\n2. Director\n3. Actors\n4. Length\n")
                chosen_filter_two = input("What filter would you like to apply?\n1. Genre\n2. Director\n3. Actors\n4. Length\n")
                search_results(search_with_filters(chosen_filter_one, chosen_filter_two, movies))
        # if they want to exit, exit the code
        if what_to_do == "3":
            break
        # if their input is invalid ask again
        else:
            continue
movie_list = load_csv()
menu(movie_list)