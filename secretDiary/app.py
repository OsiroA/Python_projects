# Personal Diary Challenge
# Author: Osi** ******E

import os, datetime, time, getpass, random
from replit import db

# Function to add a diary entry
def add():
    os.system("clear")
    timestamp = datetime.datetime.now()
    print(f"Diary entry for {timestamp}")
    diaryEntry = input("> ")
    db[timestamp] = {"entry": diaryEntry, "username": currentUser}
    time.sleep(0.5)
    os.system("clear")
    print("Diary entry added")
    time.sleep(1)
    os.system("clear")

# Function to view diary entries
def view():
    os.system("clear")
    menu = input("1. View most recent entry\n2. View specific entry by date\n> ")
    if menu == "1":
        keys = db.keys()
        for key in keys:
            time.sleep(1)
            os.system("clear")
            entry = db[key]
            print(f"""{key}:\n{entry["entry"]}""")
            print()
            option = input("Next or exit? > ")
            os.system("clear")
            if (option.lower()[0] == "n"):
                continue
    elif menu == "2":
        keys = db.keys()
        date = print("Please put the date of the entry you want (in number) in this order:")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        ojo = datetime.date(year, month, day)
        matches = [key for key in keys if key.date() == ojo]
        for match in matches:
            entry = db[match]
            print(f"""{match}:\n{entry["entry"]}""")

# Function to handle user login
def login():
    while True:
        username = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password: ")
        try:
            salt = db[username]["salt"]
            hashedPassword = hash(password + str(salt))
            if hashedPassword == db[username]["password"]:
                global currentUser
                currentUser = username
                print("Login successful")
                print("Welcome to your personal diary")
                return
            else:
                print("Login failed, try again")
        except KeyError:
            print("Username not found, please try again.")

# Function to register a new user
def register():
    while True:
        username = input("Please choose your username: ")
        if username in db:
            print("Username already exists, please choose a different one.")
            continue
        password = getpass.getpass("Please choose a password: ")
        salt = random.randint(1111, 9999)
        hashedPassword = hash(password + str(salt))
        db[username] = {"password": hashedPassword, "salt": salt}
        print(f"User {username} registered successfully")
        break

# Program execution
while True:
    if "initialized" not in db:
        register()
        db["initialized"] = True
    print("Welcome to your personal diary")
    print("1. Login\n2. Exit")
    choice = input("> ")
    if choice == "1":
        login()
        if currentUser:
            while True:
                print("1. Add Entry\n2. View Entry\n3. Logout")
                option = input("> ")
                if option == "1":
                    add()
                elif option == "2":
                    view()
                elif option == "3":
                    currentUser = None
                    break
                else:
                    print("Invalid option. Please try again.")
    elif choice == "2":
        break
    else:
        print("Invalid option. Please try again.")
