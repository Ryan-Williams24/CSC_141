# main.py
from admin import Admin

admin_user = Admin("Admin", "User")
admin_user.describe_user()
admin_user.privileges.show_privileges()