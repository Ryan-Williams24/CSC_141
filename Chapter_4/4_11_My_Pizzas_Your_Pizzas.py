my_pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']
friend_pizzas = my_pizzas.copy()

my_pizzas.append('Hawaiian')
friend_pizzas.append('Buffalo Chicken')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)