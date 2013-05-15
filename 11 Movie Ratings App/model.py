from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, types 
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, scoped_session #like sqlite3 cursor - describes how to interact with database, needs to be instantiated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine("sqlite:///ratings.db", echo=False) #creates engine that connects to db
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False)) # set a variable that will be used by sessionmaker to help interact with ratings.db, now we don't need the "connect()" function

# the variable connecting to the declarative_base function of sqlalchemy - just do it!
Base = declarative_base()
Base.query = session.query_property()

### Class declarations 

class User(Base):
	#informs sqlalchemy that an instance of this class will be stored in user table
	__tablename__ = "users"
### attributes 
	id = Column(Integer, primary_key = True) # primary key written and unique 
	email = Column(String(64), nullable=True) #nullable=True means this attribute is optional
	password = Column(String(64), nullable=True)
	age = Column(Integer, nullable=True)
	zipcode = Column(String(15), nullable=True)

	def __repr__(self):
		return u"<User: %d>"%(self.id)

class Movie(Base):
	#informs sqlalchemy that an instance of this class will be stored in "movies" table
	__tablename__ = "movies"
### attributes
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	release_at = Column(Date, nullable=True) # importing release date as a string & converting to datetime
	imdb = Column(String(64))

### "repr" function decodes the space where movie info is stored into readable text
	def __repr__(self):
		return u"<Movie: %d %s>"%(self.id, unicode(self.name))


class Rating(Base):
	__tablename__ = "ratings"

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id"))
	movie_id = Column(Integer, ForeignKey("movies.id"))
	rating = Column(Integer)
	user = relationship("User", backref=backref("ratings", order_by=id))
	movie = relationship("Movie", backref=backref("ratings", order_by=id))

### "repr" function decodes ratings info in memory space into readable text
	def __repr__(self):
		return u"<Rating: %d %d %d %d>"%(self.id, self.user_id, self.movie_id, self.rating)



	# sqlalchemy writes the init function - if we write it then it overwrites and gets odd results
	# use named parameters email = ... 

### End class declarations



def main():
    pass

if __name__ == "__main__":
    main()






