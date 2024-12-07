# Read and replace "Python" with "C"
with open('learning_python.txt') as file:
    for line in file:
        modified_line = line.replace("Python", "C")
        print(modified_line.strip())