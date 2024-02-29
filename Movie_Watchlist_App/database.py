import sqlite3
import datetime

#objects that contain sql queries for functions
CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_WATCHED_TABLE = """ CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

CREATE_USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"

INSERT_USER = "INSERT INTO users (username) VALUES (?);"

SELECT_ALL_MOVIES = "SELECT * FROM movies;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

SELECT_WATCHED_MOVIES = """ SELECT movies.* FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN users on users.username = watched.user_username
WHERE users.username = ?;"""

INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?);"

DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

SEARCH_MOVIE = "SELECT * FROM movies WHERE title LIKE ?;"

#connect to database
connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        #Create tables if they do not exist in database
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))

def add_movie(title, release_timestamp):
    with connection:
        #add movie to database
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        #check if upcoming
        if upcoming:
            #get today's time stamp
            today_timestamp = datetime.datetime.today().timestamp()
            #select movies that have a greater timestamp than today
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            #select all movies from database
            cursor.execute(SELECT_ALL_MOVIES)
        #return selected movies
        return cursor.fetchall()
    
def search_movies(search_term):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIE, (f"%{search_term}%",))
        return cursor.fetchall()

def watch_movie(username, movie_id):
        with connection:
            connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        #select all movies with watched = 1
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        #return selected movies 
        return cursor.fetchall()