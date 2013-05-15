"""
seed.py
"""
import model

db = model.connect_db()

user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "Complete my task list", user_id)

user_id = model.new_user(db, "cynthia@gmail.com", "cynpass", "Cynthia")
task = model.new_task(db, "Walk my dog", user_id)

user_id = model.new_user(db, "Liz@gmail.com", "Lizpass", "Liz")
task = model.new_task(db, "Teach classes", user_id)

user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian")
task = model.new_task(db, "Become a wizard", user_id)

user_id = model.new_user(db, "interns@hackbright.com", "internpass", "Interns")
task = model.new_task(db, "Keep being awesome", user_id)
