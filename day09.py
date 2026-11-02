password = "secret_saffffffffffaaaaaaaaaaaauce"

if len(password) < 8:
    print("Password is too short")
elif len(password) > 20:
    print("Password is too long")
else:
    print("Password accepted")
