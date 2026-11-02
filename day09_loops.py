products = ["Backpack", "Bike Light", "Bolt T-Shirt"]

for product in products:
    print(f"Checking product: {product}")
    passwords = ["abc", "secret_sauce", "12345678", "this_password_is_way_too_long_123"]

    for password in passwords:
        if len(password) < 8:
            print(f"{password} - too short")
        elif len(password) > 20:
            print(f"{password} - too long")
        else:
            print(f"{password} - accepted")