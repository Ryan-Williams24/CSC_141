current_users = ['john', 'michael', 'sara', 'alex', 'jaden']
new_users = ['John', 'anna', 'SARA', 'mike', 'chris']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")