pet1 = {'type': 'dog', 'owner': 'Alice'}
pet2 = {'type': 'cat', 'owner': 'Bob'}
pet3 = {'type': 'hamster', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()