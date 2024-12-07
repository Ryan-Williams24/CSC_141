# Ask user for their name and store it in guest.txt
guest_name = input("What is your name? ")
with open('guest.txt', 'w') as file:
    file.write(guest_name + '\n')