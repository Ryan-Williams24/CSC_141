# Using conditional test in the while loop
age = 0
while age != 'quit':
    age = input("Enter your age or 'quit' to stop: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")