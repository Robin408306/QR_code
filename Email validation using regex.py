import re

email_pattern = r"^[a-z][\w\.]*@[a-z]+\.[a-z]{2,3}$"

user_email = input("Enter your email: ")

if re.search(email_pattern, user_email):
    print("Right email")
else:
    print("Wrong email")
