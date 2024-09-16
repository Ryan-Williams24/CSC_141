invitees = ["Beyonce", "Sydney Sweeney", "Cassie Howard"]

for names in invitees: 
    print(names + ", you are invited to dinner!")

print("\n" + invitees[2] + " could not make it and will be replaced with Tokyo Toni\n")

invitees[2] = "Tokyo Toni"

for names in invitees:
    print(names + ", you are invited to dinner!")