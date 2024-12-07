# Record guest visits in guest_book.txt
while True:
    guest_name = input("What is your name? (type 'quit' to exit) ")
    if guest_name.lower() == 'quit':
        break
    with open('guest_book.txt', 'a') as file:
        file.write(guest_name + '\n')
    print(f"Hello, {guest_name}! Your visit has been recorded.")