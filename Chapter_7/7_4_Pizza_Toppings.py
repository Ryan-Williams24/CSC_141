prompt = "\nEnter a topping for your pizza (or 'quit' to stop): "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")