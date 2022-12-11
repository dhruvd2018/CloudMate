# api_key = AIzaSyAbhBUrWXioBni2BOJiataborATnRa6KtI
# Import the necessary libraries
from asyncio import Task
import flask
import sqlite3
import os
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json 



# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\Downloads\carbide-digit-371219-4ffcb9f32608.json"



# Create a Flask app object
app = flask.Flask(__name__)

# Set up the database connection
conn = sqlite3.connect('cloudmate.db')
c = conn.cursor()

# Create a table for storing user information
c.execute('''CREATE TABLE IF NOT EXISTS users (username text, password text)''')

# Load the JSON key file
with open('D:\Downloads\carbide-digit-371219-4ffcb9f32608.json') as key_file:
    key_data = json.load(key_file)

# Use the key data to create a Credentials object
creds = Credentials.from_authorized_user_file(key_data, scopes=['https://www.googleapis.com/auth/calendar'])


# Use the credentials to create a Credentials object
service = build('calendar', 'v3', credentials=creds)


# Define a route for the homepage
@app.route('/')
def home():
    # Return a simple HTML page with information about Cloud Mate
    return '<h1>Welcome to Cloud Mate!</h1><p>Cloud Mate is a cloud-based assistant for entrepreneurs that helps you schedule tasks, send emails, and manage your contacts.</p>'

# Define a route for the signup page
@app.route('/signup')
def signup():
    # Return a signup form
    return '<h1>Sign Up for Cloud Mate</h1><form action="/signup" method="POST"><label for="username">Username:</label><input type="text" id="username" name="username"><br><label for="password">Password:</label><input type="password" id="password" name="password"><br><input type="submit" value="Sign Up"></form>'

# Define a route for the signup form submission
@app.route('/signup', methods=['POST'])
def signup_submit():
    # Get the user input from the form
    username = flask.request.form['username']
    password = flask.request.form['password']

    # Add the user to the database
    c.execute('INSERT INTO users VALUES (?, ?)', (username, password))
    conn.commit()

    # Return a success message
    return '<h1>Account Created!</h1><p>Your account has been created successfully.</p>'

# Define a route for the login page
@app.route('/login')
def login():
    # Return a login form
    return '<h1>Login to Cloud Mate</h1><form action="/login" method="POST"><label for="username">Username:</label><input type="text" id="username" name="username"><br><label for="password">Password:</label><input type="password" id="password" name="password"><br><input type="submit" value="Log In"></form>'

# Define a route for the login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    # Get the user input from the form
    username = flask.request.form['username']
    password = flask.request.form['password']

    # Check if the user exists in the database
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()

    # If the user exists, return a success message
    if user:
        return '<h1>Login Successful!</h1><p>You have been logged in successfully.</p>'
    # If the user does not exist, return an error message
    else:
        return '<h1>Login Failed!</h1><p>The username or password you entered is incorrect.</p>'

# Define a route for the dashboard
@app.route('/dashboard')
def dashboard():
    # Return a dashboard page
    return '<h1>Cloud Mate Dashboard</h1><p>What would you like to do?</p><ul><li><a href="/schedule_task">Schedule a Task</a></li><li><a href="/send_email">Send an Email</a></li><li><a href="/manage_contacts">Manage Contacts</a></li></ul>'


# Define a route for scheduling a task
@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    # Get the task details from the user input
    task_title = flask.request.form['title']
    date = flask.request.form
    task_date = flask.request.form['date']
    task_time = flask.request.form['time']
    task_description = flask.request.form['description']


# Create a new event on the user's calendar
    event = {
        'summary': task_title,
        'start': {
            'dateTime': f'{Task}'
[...] 
            },
                'timeZone': 'America/New_York',

            },
    'end'
    
    {   
        'dateTime': f'{task_date}T{task_time}:00',
        'timeZone': 'America/New_York',
            }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    
    # Return a success message
    return '<h1>Task Scheduled!</h1><p>Your task has been scheduled successfully.</p>'

# Define a route for sending an email
@app.route('/send_email', methods=['POST'])
def send_email():
   
    # Get the email details from the user input
    email_to = flask.request.form['to']
    email_subject = flask.request.form['subject']
    email_body = flask.request.form['body']
    def create_message(to: str, subject: str, body: str) -> str:
        # Create a message with the specified recipient, subject, and body
        message = f'To: {to}\nSubject: {subject}\n\n{body}'
        return message
    def send_message(message: str):
        pass
    def send_email(email_to: str, email_subject: str, email_body: str):   
        # Send an email to the specified recipient
        message = create_message(email_to, email_subject, email_body)
        send_message(message)
        # Return a success message
        return '<h1>Email Sent!</h1><p>Your email has been sent successfully.</p>'
    # Define a route for managing contacts
@app.route('/manage_contacts')
def manage_contacts():
    # Return a page with a list of contacts
    return '<h1>Manage Contacts</h1><p>Here is a list of your contacts.</p><ul><li>John Smith</li><li>Jane Doe</li></ul>' 

# Run the Flask app
app.run(host= "Localhost",
    port=8080)




