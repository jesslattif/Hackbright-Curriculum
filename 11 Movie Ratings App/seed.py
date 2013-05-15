import model
import csv
from datetime import datetime

#for each table:     
"""open a file
read a line
parse a line
create an object
add the object to a session
commit
repeat until done"""


_ID = 0 # setting global id variable to use when referencing in lists index


def load_users(session):
    # use u.user
    # setting variables for numbers we will reference in lists - so we can pass them through later as the variable name    
    _AGE = 1
    _ZIP = 4

    users_file = open("seed_data/u.user")   # opens file as an object 
    parser = csv.reader(users_file, delimiter="|") # splits object into rows where each row is a list of strings
    for row in parser: # pull one row out of the object
        user = model.User(id=row[_ID], age=row[_AGE], zipcode=row[_ZIP])
        session.add(user) # add the user to sesion to pass it to the db
    session.commit() # commit the change to the db


def load_movies(session):
    # use u.item
    _NAME = 1
    _RELEASE = 2 #
    _IMDB = 4

    movies_file = open("seed_data/u.item")   # opens item file as an object 
    parser = csv.reader(movies_file, delimiter="|") # splits object into rows where each row is a list of strings
    for row in parser:
        if row[_RELEASE]:
            release_date = datetime.strptime(row[_RELEASE], "%d-%b-%Y") # converts string into "day-month-year" format, also ignores that field if no value entered.
        else:
            release_date = None
        decode_row = row[_NAME]
        decode_row = decode_row.decode("latin-1")
        movie = model.Movie(id=row[_ID], name=decode_row, release_at=release_date, imdb=row[_IMDB])
        session.add(movie)
    session.commit()


def load_ratings(session):
    # use u.data
    _MOVIE_ID = 1
    _RATING = 2
    
    ratings_file = open("seed_data/u.data") # opens ratings file & captures as a variable
    parser = csv.reader(ratings_file, delimiter="" or "\t") #parses through each row, splitting along spaces or tabs

    for row in parser:
        ratings = model.Rating(user_id=row[_ID], movie_id=row[_MOVIE_ID], rating=row[_RATING]) #sets items in row lists equivalent to column values in Ratings table from model.py
        session.add(ratings) #adds to database
    session.commit() # commits to database


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    #load_users(session)
    #load_movies(session)
    #load_ratings(session)
    pass

if __name__ == "__main__":
    session = model.connect()
    main(session)

