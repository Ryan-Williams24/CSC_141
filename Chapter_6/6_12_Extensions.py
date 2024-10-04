cities = {
    'new york': {
        'country': 'usa',
        'population': 8419600,
        'fact': 'Known for Times Square.'
    },
    'london': {
        'country': 'uk',
        'population': 8982000,
        'fact': 'Home to the British Museum.'
    },
    'sydney': {
        'country': 'australia',
        'population': 5230330,
        'fact': 'Famous for the Sydney Opera House.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")

cities['new york']['founded'] = 1624
cities['london']['founded'] = 43
cities['sydney']['founded'] = 1788

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")