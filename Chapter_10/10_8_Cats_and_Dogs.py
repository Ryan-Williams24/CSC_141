# Read and print the contents of cats.txt and dogs.txt with error handling
try:
    with open('cats.txt') as file:
        print("Cats:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Sorry, cats.txt file not found.")

try:
    with open('dogs.txt') as file:
        print("\nDogs:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Sorry, dogs.txt file not found.")