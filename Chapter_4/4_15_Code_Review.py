# 4_3_counting_to_twenty
for value in range(1, 21):
    print(value)

# 4_4_one_million
million_numbers = list(range(1, 1000001))
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

# 4_8_cubes
cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
for cube in cubes:
    print(cube)