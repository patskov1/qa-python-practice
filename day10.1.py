users = [
    {"username": "standard_user", "is_locked": False},
    {"username": "locked_out_user", "is_locked": True},
    {"username": "problem_user", "is_locked": False}
]

def check_user(user):
    if user["is_locked"]:
        print(f"{user['username']} - cannot log in")
    else:
        print(f"{user['username']} - can log in")

for user in users:
    check_user(user)