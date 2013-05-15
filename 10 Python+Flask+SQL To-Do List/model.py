"""
model.py
"""
import sqlite3
import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")


def new_user(db, email, password, name):          
    c = db.cursor()     #creates cursor at lines you want                                
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    result = c.execute(query, (email, password, name))   # c.execute always needs a tuple of stuff you're entering!   
    db.commit() #commit to database
    return result.lastrowid #returns ID (primary key) of user you created


def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?""" 
    c.execute(query, (email, password))
    result = c.fetchone() # fetchone gets one row from db
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))
        #zip creates a tuple from the lists inserted starting with index [0]
    return None


def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """SELECT * from Users WHERE id = ?"""
    c.execute(query, (user_id))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"] #tells which fields to return
        return dict(zip(fields,result)) #returns a dictionary of fields with their corresponding results


def new_task(db, title, user_id):
    """Given a title and a user_id, create a new task belonging to that user. Return the id of the created task"""
    c = db.cursor()
    time_created = datetime.datetime.today() #sets a date & time the task was created when function is called
    query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
    result = c.execute(query,(title, time_created, user_id))
    db.commit()
    return result.lastrowid #returns the ID (primary key) of the new task


def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    time_completed = datetime.datetime.now() #sets time completed when function is called
    query = """UPDATE Tasks SET completed_at=? WHERE id = ?""" #updates db
    result = c.execute(query,(time_completed, task_id))
    db.commit()


def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    c = db.cursor()
     

    if user_id == None: #if not given any user id, query selects all tasks
        query = """SELECT * FROM Tasks"""
        c.execute(query,())
        
    else:
        query = """SELECT * FROM Tasks WHERE user_id = ?""" #with user id, selects tasks for that user
        c.execute(query, (user_id))
    
    result = c.fetchall() #result can be one, many or none

    if result: #if task(s) exist from the query
        fields = ['id','title','created_at', 'completed_at', 'user_id'] #creates a list of fields
        tasks = [] #creates a list of tasks
        for rows in result:
            task = dict(zip(fields, rows)) # makes each row in the results a dictionary
            tasks.append(task) # appends the new dict to the empty list tasks
        return tasks # returns the tasks as a list of dictionaries
    else:
        print "No tasks exist"
        

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""
    c = db.cursor()
    query = """SELECT * FROM Tasks WHERE id = ?""" #selects task(s) from particular user id
    c.execute(query,(task_id))
    result = c.fetchone() 
    if result: #if task(s) exist for that user
        fields = ["id", "title", "created_at", "completed_at", "user_id"] #creates a list of fields
        return dict(zip(fields, result)) # matches fields to results & zips into a dictionary
