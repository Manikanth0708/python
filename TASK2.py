import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

email_input = input("Enter an email address: ")


if is_valid_email(email_input):
    print("Valid email.")
else:
    print("Invalid email.")

