browsers = ("chromium", "firefox", "webkit")
print(browsers[0])
print(len(browsers))


users = {"standard_user", "problem_user", "standard_user"}
print(users)
print(len(users))


email = "  TEST@Mail.com  "
print(email.strip())
print(email.strip().lower())


error = ("Epic sadface: Username is required")
print("required" in error)
parts = error.split(":")
print(parts[1])
username = " Standard User "
print(username.strip().lower())