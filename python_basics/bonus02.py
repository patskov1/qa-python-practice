age_text = "25"

try:
    age = int(age_text)
    print(f"Age: {age}")
except ValueError:
    print("Please enter a number")

print("Done")


def convert_price(text):
    try:
        price = float(text)
        print(f"Price: {price} EUR")
    except ValueError:
        print("Invalid price")

convert_price("19.99")
convert_price("free")


def check_password(password):
    if len(password) >= 8:
        print("Password accepted")
    else:
        print("Password is too short")


check_password("abc")
check_password("secret_sauce")


def check_password(password):
    if len(password) >= 8:
        print("Password accepted")
    else:
        print("Password is too short")


passwords = ["abc", "secret_sauce", "12345678", "qwerty"]

for password in passwords:
    check_password(password)