# Read and print the contents of cats.txt and dogs.txt with silent failure
try:
    with open('cats.txt') as file:
        print("Cats:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    pass

try:
    with open('dogs.txt') as file:
        print("\nDogs:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    pass