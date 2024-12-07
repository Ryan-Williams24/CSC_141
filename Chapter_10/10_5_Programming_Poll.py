# Record reasons why people like programming
while True:
    reason = input("Why do you like programming? (type 'quit' to exit) ")
    if reason.lower() == 'quit':
        break
    with open('programming_poll.txt', 'a') as file:
        file.write(reason + '\n')