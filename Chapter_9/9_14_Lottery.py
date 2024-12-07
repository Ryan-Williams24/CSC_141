import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Select 4 random items
winners = random.sample(lottery_items, 4)

print(f"Winning ticket includes: {winners}")