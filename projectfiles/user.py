class User:
	def __init__(self, name, password):
		#initializes a user with am empty list of tasks available and tasks completed
		self.name = name
		#private instance variable for user's password
		self.__password = password
		#private instance variable for available tasks
		self.__tasks = []
		#private instance variable for completed tasks
		self.__c_tasks = []


	def add_task(self, task):
		#task: Task object from task.py
		#adds this task to the user queue of tasks to complete
		#return type: None

	def remove_task(self, task):
		#task: is a Task object from task.py
		#removes this task from the tasks queue
		#return type: None
	
	def task_completed(self, task):
		#task: Task object from task.py
		#removes task and adds it to the completed category
		#return type: None

	def get_tasks_status(self):
		#returns all of the the completed tasks under the section completed and all of the tasks available under the status pending
		#return type list	

	def get_tasks_available(self):
		#return a list of the tasks that are still left to do
		#return type list
	
	def change_password(self, new_password): 	
		#sets the password to the new password the user types
		#return type: None

	@staticmethod
	def create_user(username, password, password_confirm):
		#check if username is in database
		#check if password meets requirements

	@staticmethod
	def login(username, password):
		#if login credentials are valid returns the corresponding user's information to that user
	@staticmethod	
	def check_password(password, password_confirm):
		#checks if the password is valid	




