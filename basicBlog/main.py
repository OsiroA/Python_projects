from flask import Flask, redirect, render_template, request, url_for
import os
import datetime

app = Flask(__name__)
ENTRIES_FILE = 'entries.txt'

my_secret = os.environ['Blogadminpassword']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            if username == "Osiro" and password == my_secret:
                return redirect(url_for('display'))  # Redirect to display page after successful login
        except TypeError as e:
            print(f"The following error occurred:\n{e}")
    return render_template('login.html')

@app.route('/display')
def display():
    entries = []
    try:
        with open(ENTRIES_FILE, 'r') as file:
            lines = file.readlines()
            entry = {}
            for line in lines:
                line = line.strip()
                if line.startswith('Date:'):
                    if entry:
                        entries.append(entry)
                        entry = {}
                    entry['Date'] = line[len('Date:'):].strip()
                elif line.startswith('Heading:'):
                    entry['Heading'] = line[len('Heading:'):].strip()
                elif line.startswith('Body:'):
                    entry['Body'] = line[len('Body:'):].strip()
                elif line.startswith('Image:'):
                    entry['Image'] = line[len('Image:'):].strip()
            if entry:
                entries.append(entry)
    except FileNotFoundError:
        print("No entries found.")
    return render_template('display.html', entries=entries)
  
@app.route('/input', methods=["POST", "GET"])
def input():
    if request.method == "POST":
        try:
            heading = request.form.get('heading')
            body = request.form.get('body')
            image = request.form.get('image')
            date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            with open(ENTRIES_FILE, 'a') as file:
                file.write(f"Date: {date}\nHeading: {heading}\nBody: {body}\nImage: {image}\n\n")
            return redirect(url_for('display'))
        except TypeError as e:
            print(f"The following error occurred:\n{e}")
    elif request.method == "GET":
        # Render input form only when the request method is GET
        return render_template('input.html', date=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    # Redirect to login page if the request method is neither GET nor POST
    return redirect(url_for('login'))

app.run(host='0.0.0.0', port=81)
