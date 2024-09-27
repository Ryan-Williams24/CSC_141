items = ['Mount Everest', 'Amazon River', 'Canada', 'Tokyo', 'Spanish']

print("\nOriginal list:", items)

print("\nNumber of items in the list:", len(items))

print("\nSorted list (alphabetical):", sorted(items))

print("\nList after sorted():", items)

items.reverse()
print("\nList after reverse():", items)

items.sort()
print("\nList after sort():", items)

items.append('Australia')
print("\nList after append():", items)

items.insert(2, 'Nile River')
print("\nList after insert():", items)

removed_item = items.pop()
print(f"\nRemoved item: {removed_item}")
print("List after pop():", items)

del items[3]
print("\nList after del:", items)