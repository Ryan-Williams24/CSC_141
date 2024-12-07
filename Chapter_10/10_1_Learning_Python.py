# Read the file and print it in three different ways
# Create the file learning_python.txt
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can create variables and assign values.\n")
    file.write("In Python you can define functions to organize code.\n")
    file.write("In Python you can use loops to repeat tasks.\n")
    file.write("In Python you can handle exceptions to deal with errors.\n")
# 1. Print the entire file content
with open('learning_python.txt') as file:
    content = file.read()
    print("Entire file content:")
    print(content)

# 2. Loop through each line and print
with open('learning_python.txt') as file:
    print("\nLoop through lines:")
    for line in file:
        print(line.strip())

# 3. Store lines in a list and print
with open('learning_python.txt') as file:
    lines = file.readlines()
    print("\nList of lines:")
    for line in lines:
        print(line.strip())