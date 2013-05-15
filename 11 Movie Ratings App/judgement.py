
from flask import Flask, render_template, redirect, request, session, url_for
import model
from model import User, Item, Trade, Participant, session as db_session

app  = Flask(__name__)
app.secret_key = "BlahhhBlahSECRETBllllaH"


"""Index"""

@app.route("/")
def index():
	return render_template("index.html")

	"""Sign up page"""


@app.route("/sign_up")
def sign_up():
	return render_template("sign_up.html")


"""Create a new user"""

@app.route("/new_user", methods=["POST"])
def save_new_user(): 
	new_user = User(email=request.form["email"], password=request.form["password"], age=request.form["age"], zipcode=request.form["zipcode"])#new instance of class "User", fields filled in from web form
	db_session.add(new_user) #add & commit new user
	db_session.commit()
	user_email = new_user.email
	return render_template("new_user.html", user_email=user_email)


"""Log-in"""

@app.route("/log_in")
def log_in():
	return render_template("log_in.html")


"""Authenticate User"""

@app.route("/authenticate", methods=["POST"])
def authenticate(): # authenticate user
	email = request.form['email']
	password = request.form['password']
	user = db_session.query(User).filter_by(email=email, password=password).first() #checks for user in db

	if not user: #redirect to log-in if info not correct
		print "FAILED LOGIN"
		return redirect("/log_in")

	print "SUCCEEDED" 
	session["user_id"] = user.id #set session
	return redirect("/my_homepage") #redirects to user's movie ratings page for unique user id


"""Go to user's homepage"""

@app.route("/my_homepage")
def go_to_homepage():
	user_id = session.get("user_id") #gets user ID from current session
	if not user_id: # redirects to log-in if no user ID session
		return redirect("/log_in")

	return render_template("my_homepage.html")

"""See list of all users"""

@app.route("/user_list")
def list_users(): #lists all users, limited to first 5
	user_list = db_session.query(User).limit(5).all()
	print user_list
	return render_template("user_list.html", user_list=user_list)

"""View ratings of a particular user"""

@app.route("/view_ratings/<int:id>")
def view_user_ratings(id): #views ratings of a particular user (by ID), limited to first 10 ratings
	user_ratings = db_session.query(Rating).filter_by(user_id=id).limit(10).all()
	return render_template("view_ratings.html", ratings = user_ratings)

"""Search for movies to rate"""

@app.route("/search", methods=["GET"])
def search_by_name(): #search for movies by movie name
	user_id = session.get("user_id") #gets user ID from current session
	search_term = request.args.get("search_term", '')
	if search_term == '':
		return render_template("search.html")
	movies = db_session.query(Movie).filter(Movie.name.like("%" + search_term + "%")).all()
	return render_template("search_results.html", 
		movies=movies, 	
		search_term=search_term)	

"""View one's own movie ratings (must be logged in)"""

@app.route("/get_my_ratings")
def get_my_ratings():
	user_id = session.get("user_id") #gets user ID from current session
	if not user_id: # redirects to log-in if no user ID session
		return redirect("/log_in")

	user = db_session.query(User).get(user_id)
	ratings = user.ratings #gets ratings for user id
	return render_template("get_my_ratings.html", 
							user=user, 
							ratings=ratings)

""" Display a movie's rating"""
@app.route("/movie/<int:id>", methods=["GET"])
def display_movie(id):
	user_id = session.get("user_id") #gets user ID from current session
	if not user_id: # redirects to log-in if no user ID session
		return redirect("/log_in")
	movie = db_session.query(Movie).get(id)

	return render_template("update_rating.html", 
							movie=movie, 
							user_id=user_id)

@app.route("/movie/<int:id>", methods=["POST"])
def update_rating(id):
	user_id = session.get("user_id") #gets user ID from current session
	if not user_id: # redirects to log-in if no user ID session
		return redirect("/log_in")
	user = db_session.query(User).get(user_id) #getting user cuz u need it
	movie = db_session.query(Movie).get(id) #double-checking that movie id matches movie in db
	rating_num = int(request.form["rating"]) #takes in rating as an integer
	new_rating = Rating(rating=rating_num) #creates new rating object from user's rating
	new_rating.user = user #attach user object to rating object
	new_rating.movie = movie #attach movie object to rating object

	db_session.commit()
	#commit to db
	return redirect("/get_my_ratings")





if __name__ == "__main__":
	app.run(debug = True)

