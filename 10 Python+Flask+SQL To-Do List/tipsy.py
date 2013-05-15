"""
tipsy.py -- A flask-based to-do list!
"""

from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", first_name = "")

@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks = tasks_from_db)

@app.route("/new_task")
def new_tasks():
	return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
	task_title = request.form['task_title']
	user_id = request.form['user_id']
	db = model.connect_db()
# assume all tasks are attached to user 1 :(
	task_id = model.new_task(db, task_title, user_id)
	return redirect("/tasks")

if __name__ == "__main__":
	app.run(debug=True)


