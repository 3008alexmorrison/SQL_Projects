import database
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add new user
7) Exit.

Your selection: """

welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()

#functions for menu options
def prompt_add_movie():
    #prompt for title and release date
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    #parse release date into timestamp for later use
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    #add movie to database
    database.add_movie(title, timestamp)

def timestamp_to_date(timestamp):
    #unparse timestamp into default format date
    date = datetime.datetime.fromtimestamp(timestamp)
    #format date into more readable format and convert to string
    formatted_date = date.strftime("%B %d, %Y")
    return formatted_date

def print_movie_list(heading, movies):
    #header
    print(f"-- {heading} Movies --")
    #iterate through database to get specified movies
    for _id, title, release_date in movies:
        #format timestamp to readable date
        date_of_release = timestamp_to_date(release_date)
        #print movie list
        print(f"{_id}: {title} | Released On: {date_of_release}")
    print("--- \n")

def print_watched_movie_list(watcher_name, movies):
    print(f"-- {watcher_name}'s watched movies --")
    for movie in movies:
        print(f"{movie[1]}")
    print("---- \n")

def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_watch_movie():
    #Who are you and what was the movie that you watched?
    username = input("Please enter your username: ")
    movie_id = input("Movie ID: ")
    #mark watched
    database.watch_movie(username, movie_id)

#Menu while loop
while (user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        watcher_name = input("Please enter your name: ")
        movies = database.get_watched_movies(watcher_name)
        print_watched_movie_list(watcher_name, movies)
    elif user_input == "6":
        prompt_add_user()
    else:
        print("Invalid input, please try again!")