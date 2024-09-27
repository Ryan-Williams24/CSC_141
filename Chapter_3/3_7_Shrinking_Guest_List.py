invitees = ["Beyonce", "Sydney Sweeney", "Cassie Howard"]
removed = []

for names in invitees: 
    print(names + ", you are invited to dinner!")

print("\n" + invitees[2] + " could not make it and will be replaced with Tokyo Toni\n")

invitees[2] = "Tokyo Toni"

for names in invitees:
    print(names + ", you are invited to dinner!")

print("\nA bigger table has been acquired and more people can be seated.")

invitees.insert(0, "Gerald")
invitees.insert(2, "Deni")
invitees.append("Kamala Harris")

for names in invitees:
    print(names + ", you are invited to dinner!")

print("\nI can only invite two people for dinner")

while len(invitees) > 2:
    removed_person = invitees.pop()  
    removed.append(removed_person)   
    print(removed_person + ", you have been removed from the invite list.")

print("\n")

for person in invitees:
    print(person + ", you are still invited.")

while invitees:
    del invitees[-1]

print("\nFinal guest list:", invitees)