polling = True
responses = {}

while polling:
    name = input("\nWhat's your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("Would you like another person to respond? (yes/no) ")
    if repeat == 'no':
        polling = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")