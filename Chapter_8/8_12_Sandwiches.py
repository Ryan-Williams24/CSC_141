def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("lettuce", "tomato", "bacon")
make_sandwich("ham", "cheese")
make_sandwich("turkey", "mayo", "mustard", "avocado")