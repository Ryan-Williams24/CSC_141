import json

# Store favorite number
favorite_number = input("What is your favorite number? ")
with open('favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)

# Retrieve favorite number
with open('favorite_number.json') as file:
    favorite_number = json.load(file)
    print(f"I know your favorite number! It's {favorite_number}.")