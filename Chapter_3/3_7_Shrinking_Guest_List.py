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

print("I can only invite two people for dinner")

for i in invitees: 
    if removed < [4] :
        removed.append(i)
        invitees.pop([i])
        print(i + ", you have been removed.")