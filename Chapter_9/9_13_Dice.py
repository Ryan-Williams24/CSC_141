import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

six_sided = Die()
ten_sided = Die(10)
twenty_sided = Die(20)

print("Rolling 6-sided die 10 times:")
for _ in range(10):
    print(six_sided.roll_die())

print("Rolling 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided.roll_die())

print("Rolling 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided.roll_die())