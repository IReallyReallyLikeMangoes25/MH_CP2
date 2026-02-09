# MH 2nd Movie recommender project
import csv
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
        if desired_genre in movies["Genre"]:
            movies_with_genre.append(movie)
    # return the list of movies with that genre
    return movies_with_genre

# function for searching for director:
    # ask user what director they are looking for
    # loop through the director section of the file and if any movies were made by that director add them to a list inside this function
    # return the list of all movies with that director

# function for searching for actors:
    # ask user how many actors they will be searching for
    # ask for the names of how ever many actors they are searching for
    # loop through the file ad if any movie has any of those actors save it to a list in this function
    # return the list of movies with selected actors

# function for searching for length:
    # ask if they want to search for minimum, maximum, or both
    # if they say minimum ask for the minimum length and set maximum to infinite
    # if they say maximum ask for maximum length and set minimum to 0
    # if they say both ask for both
    # loop through the file and if a movie has a length somewhere inbetween the max and min
    # if it does add it to a list of movies inside of this function
    # return the list of movies

# function for searching using selected filters, takes in what filters they chose:
    # if they chose to search for genre run the search for genre function
    # if they chose to search for director run the the search for director function
    # if they chose to search for actors run the search for actors function
    # if they chose to search for lenght run the search for length function
    # take the two lists that were returned by two of the functions and loop over both, seeing if any movies are in both
    # if a movie is in both add it to a new list inside this function
    # return the list of movies

# print search results function, takes in list of movies:
    # loops over list printing movies one by one

# print full list function:
    # loops over list printing movies one by one

# menu function:
    # ask is user wants to print the full list, search, or exit
    # if they want to print the full list run the print full list function
    # if they want to search print search options
    # ask if they will be searching for one or two filters
    # if they choose one ask for it then run the corresponding search function and print the resuts with the print searvch results function
    # if they want to search for two ask user for both and run the search using selected filters function and print the results with the print search results function
    # if they want to exit, exit the code
    # if their input is invalid ask again