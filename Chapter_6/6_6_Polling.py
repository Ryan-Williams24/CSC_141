favorite_languages = {
    'bob': 'python',
    'bill': 'c',
    'steve': 'ruby',
    'phil': 'python'
}

people_to_poll = ['bob', 'steve', 'michael', 'bill', 'anna']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, you are invited to take the favorite languages poll.")