# Task Manager (Name can be changed later)
Here user's can create accounts with password protection. (passwords must be hashed in our databases) and keep track of a list of tasks they need to do. This will start as web application using Flask for the backend, PostgreSQL for the database and React JS for the front end.

This will be a single-page web application using React Router. We will have the following pages. If Derek Teske thinks changing this structure will be better then we can discuss those changes.

1. Login/Register Page
2. Main Dashboard Page (after user logs in)
    1. One section displays their tasks and allows them to mark them as completed by clicking on a button.
    2. Another section will allow them to create a task.
    3. Another section will let them generate a list of tasks after they input the amount of free time they have. 
    4. Link or toggle to view previous logs.
3. Settings Page (can be a tab as well).

# Key Features

1. Users can manage their accounts.
    1. Create account
    2. Login / Logout
    3. Change password.
    4. Recover account (optional if you want to add emails.)
2. Once signed in, users can do the following with tasks.
    1. Create a new task.
    2. Mark that they have completed a task.
    3. View their currently unfinished tasks.
    4. View their previously finished tasks.
    5. Can input how much time they currently have and have a series of tasks they can complete in the given time frame. 
    6. Delete a task without marking it as complete.

# Roles
1. Back-end in Flask and PostgreSQL (Kelvin)
2. Front-end in React JS (Derek Teske)
3. Hosting on Heroku (Darek Johnson)

# Back End Milestones
1. Setup Flask server to handle GET and POST requests.
2. Design necessary Flask routes for the application, but do not implement fully. 
3. Test said routes with dummy data to make sure the routes are being called correctly.
4. Design necessary classes and APIs of those classes to be used in the HTTP request handlers.
5. Implement said classes using [Flask SQL Alchemy](http://flask-sqlalchemy.pocoo.org/2.3/) and a PostgreSQL database. Also implement any helper classes such as jwt_util for security.
6. Write unit tests for the classses.
7. Integrate the classes with the HTTP handlers.
8. Write unit tests for the HTTP handlers. 

# Front End Milestones

1. Setup a react application using webpack.
2. Create a react component for each page. For now ignore sending HTTP requests - you can add these in later. To test individual pages, you can create dummy variables to display information on the pages. This way you can start setting up the structure of the front end as incremental progress is made on the back end. This will probably take the most time because you are designing the entire front end UI. Do not move on to the next step until it looks presentable according to Kelvin.
3. Integrate the HTTP requests into front end control flow. Kelvin should have some of these completed, but if he doesn't then you can add in the handlers as though they are done. Feel free to make feature requests to Kelvin if any of the APIs need to be changed to help with the front end. 
4. At this point we should have a working version of a web application. Now is the time to do quality assurance as a user to make sure there are no obvious bugs.

# What is a task?
1. Name of task.
2. Description of task.
3. Estimated time to complete task.
4. Deadline when it must be completed by.
5. Time it was created.
6. Whether or not it is completed.
7. If completed, time of completion.

# What is a user?
1. Name of user.
2. Password hash of user.
3. user_id - unique id  to identify users.

# What HTTP requests do we need to handle?
1. Create Account
2. Check Login
3. Change Password
4. Create Task
5. Delete Task
6. Mark Task as Complete
7. Get List of Tasks To Do Now
8. Get Tasks (completed and pending)
