# 4_10_slices.py
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken', 'Hawaiian', 'Veggie']

print("The first three items in the list are:", pizzas[:3])
middle_index = len(pizzas) // 2
print("Three items from the middle of the list are:", pizzas[middle_index-1:middle_index+2])
print("The last three items in the list are:", pizzas[-3:])