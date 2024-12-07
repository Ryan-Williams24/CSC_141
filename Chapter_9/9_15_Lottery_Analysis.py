import random

lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [3, 'd', 7, 9]  # The ticket you want to match

# Keep pulling numbers until we get a match
draw_count = 0
while True:
    draw_count += 1
    drawn_items = random.sample(lottery_items, 4)
    if drawn_items == my_ticket:
        break

print(f"It took {draw_count} attempts to win with ticket {my_ticket}")