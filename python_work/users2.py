class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0
    def increment_login_attempts(self):
        self.login_attempt += 1
    def reset_login_attempts(self):
        self.login_attempt = 0
    def describe_user(self):
        print(f"Hi, my first name is {self.first_name} and my last name is {self.last_name}")
    def greet_user(self):
        print(f"Congratulations {self.first_name}")

user1 = User("Vitor", "Silva")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user1.greet_user()