class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("standard_user", "secret_sauce")
user2 = User("problem_user", "secret_sauce")

print(user1.username)
print(user2.username)
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show_info(self):
        print(f"Username: {self.username}, Password: {self.password}")

user1 = User("standard_user", "secret_sauce")
user2 = User("problem_user", "secret_sauce")

user1.show_info()
user2.show_info()
import requests
class LoginPage:
    def __init__(self):
        self.url = "https://www.saucedemo.com"

    def open(self):
        print(f"Opening {self.url}")

    def login(self, username, password):
        print(f"Entering username: {username}")
        print(f"Entering password: {password}")
        print("Clicking Login button")

page = LoginPage()
page.open()
page.login("standard_user", "secret_sauce")
response = requests.get("https://restful-booker.herokuapp.com/booking/1")
print(response.status_code)
print(response.json())