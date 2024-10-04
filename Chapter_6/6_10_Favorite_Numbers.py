favorite_numbers = {
    'Gerald': [7, 13],
    'Deni': [3, 8, 20],
    'Aniyah': [5],
    'Stephanie': [9, 12],
    'Adriel': [11, 22, 33]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}.")
