def greet(name):
    print(f"Hello, {name}!")

greet("Vadym")
greet("standard_user")
def calculate_total(price, nights):
    return price * nights

total = calculate_total(50, 4)
print(total)
print(total > 150)
error = get_error_text()
assert error == "Epic sadface: Username is required"
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