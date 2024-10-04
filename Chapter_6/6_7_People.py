person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 22,
    'city': 'London'
}

person3 = {
    'first_name': 'Steve',
    'last_name': 'Jobs',
    'age': 35,
    'city': 'Sydney'
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()