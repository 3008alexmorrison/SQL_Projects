import sqlite3
import datetime

#objects that contain sql queries for functions
CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL
);"""

CREATE_WATCHLIST_TABLE = """ CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"

SELECT_ALL_MOVIES = "SELECT * FROM movies;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"

INSERT_WATCHED_MOVIE = "INSERT INTO watched (watcher_name, title) VALUES (?, ?);"

DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

#connect to database
connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        #Create tables if they do not exist in database
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)

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

def watch_movie(watcher_name, title):
        with connection:
            connection.execute(DELETE_MOVIE, (title,))
            connection.execute(INSERT_WATCHED_MOVIE, (watcher_name, title))

def get_watched_movies(watcher_name):
    with connection:
        cursor = connection.cursor()
        #select all movies with watched = 1
        cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
        #return selected movies 
        return cursor.fetchall()