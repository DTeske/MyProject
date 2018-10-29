from flask import Flask, jsonify, request

app = Flask(__name__)

usernames = [{'name': 'Kelvin'}, {'name' : 'Darek'}]

@app.route('/', methods=['GET'])
def hello():
	return 'Hello World!'

@app.route('/signup', methods=['POST'])
def newaccount():
	input = username, password

	output = 1. take them to a page that tells them signup was successful
			 2. does not meet the requirements for making an account

	description = the server/database needs to store the username and password


@app.route('/login_user', methods=['POST'])
def login_user():
	"""
	input = username, password
	output = login successful, login failure
	description = sends information to the server to verify - but does not add new info to database
	"""
@app.route('/change_password', methods=['POST'])
def change_password():
	"""
	input = new password
	output = password change successful, valid password, invalid password
	description = sends information to server/database and stores the new password to the existing username
	"""
@app.route('/create_task', methods=['POST'])
def create_task():

	"""
	input = task/goal: (all attributes of task laid out in what is a task refer to design doc)
	output = task creation successful
	description = sends information to server/database and stores the new task to the existing username
	"""
@app.route('/delete_task', methods=['POST'])
def delete_task():
	"""
	input = click or type in task to be deleted
	output = are you sure you want to delete this item?, delete successful
	description = sends information to server/database and store deletes the task associated to the existing username		
	"""
@app.route('/task_complete', methods=['POST'])
def completed_task():

	"""
	input = click or type in task to be checked and marked completed
	output = Task completed
	description = sends information to server/database and store the task associated to the existing username as completed
	"""
@app.route('/get_tasks_available', methods=['POST'])
def get_task_avilable():
	"""
	input = click or type in a specific task or click or type in available tasks
	output = return task from the queue or return the whole list of tasks
	description = does not really change database
	"""
@app.route('/get_tasks_status', methods=['POST'])
def get_tasks_status():
	"""
	input = click or type in pending or completed or all tasks status
	output = list of completed tasks or pending tasks or all tasks with the status of c or p next to them
	description = does not really change database
	"""
if __name__ == '__main__':
	app.run(debug=True)