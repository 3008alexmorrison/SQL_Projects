import sqlite3
import datetime

#objects that contain sql queries for functions
CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"

SELECT_ALL_MOVIES = "SELECT * FROM movies;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"

SELECT_WATCHED_MOVIES = "SELECT * FROM moveies WHERE watched = 1;"

SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"

#connect to database
connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        #Create tables if they do not exist in database
        connection.execute(CREATE_MOVIES_TABLE)

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

def watch_movie(title):
    with connection:
        cursor = connection.cursor()
        #Update movie in database to switch watched 0 to 1
        cursor.execute(SET_MOVIE_WATCHED, (title,))

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        #select all movies with watched = 1
        cursor.execute(SELECT_WATCHED_MOVIES)
        #return selected movies 
        return cursor.fetchall()