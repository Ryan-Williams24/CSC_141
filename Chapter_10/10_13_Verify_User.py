# Verify and get username
import json

def greet_user():
    try:
        with open('username.json') as file:
            username = json.load(file)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open('username.json', 'w') as file:
            json.dump(username, file)
    
    correct_username = input(f"Is {username} your username? (y/n) ")
    if correct_username.lower() != 'y':
        username = input("Please enter your correct username: ")
        with open('username.json', 'w') as file:
            json.dump(username, file)
    
    print(f"Hello, {username}!")

greet_user()