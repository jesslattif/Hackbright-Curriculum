import sqlite3

DB = None
CONN = None

def make_new_project(new_title, new_description, new_max_grade): #hyphenate or underscore between words in description to avoid splitting into the list
    query = """ INSERT INTO Projects values (?, ?, ?)""" 
    DB.execute(query, (new_title, new_description, new_max_grade))
    CONN.commit()
    print "Successfully added project: %s" % new_title

def get_grade_on_project(choose_student, their_project): #enter student's github name
    query = """SELECT grade FROM Grades WHERE student_github = ? AND project_title = ?"""
    DB.execute(query, (choose_student,their_project))
    row = DB.fetchone()
    print """\
    Grade is %s """ % row[0]

def give_grade_on_project(project_name, student_grade, their_github):
    query = "INSERT INTO Grades values (?, ?, ?)"
    DB.execute(query, (their_github, project_name, student_grade))
    CONN.commit()
    print "Successfully added student's grade %s on %s." % (student_grade, project_name)


def get_projects_by_title(some_title):
    query = """ SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (some_title,))

    row = DB.fetchone() # row = ("Markov", "Tweets...", 50)
    # row[0] => Markov
    # row[1] => Tweets...
    # row[2] => 50

    print """\
    Project: %s
    Description: %s
    Maximum Grade: %d""" %(row[0], row[1], row[2])

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
        Student: %s %s 
        Github account: %s""" %(row[0], row[1], row[2])

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" %(first_name, last_name)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("my_database.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) # why is it *args?
        elif command == "new_student":
            make_new_student(*args)
        elif command == "title":
            get_projects_by_title(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "get_grade":
            get_grade_on_project(*args)
        elif command == "add_grade":
            give_grade_on_project(*args)



    CONN.close()

if __name__ == "__main__":
    main()
