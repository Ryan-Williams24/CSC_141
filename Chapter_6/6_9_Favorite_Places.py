favorite_places = {
    'Gerald': ['paris', 'new york', 'tokyo'],
    'Deni': ['london', 'barcelona'],
    'Aniyah': ['sydney', 'dubai']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
    print()