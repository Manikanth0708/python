import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("User already exists")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login(username, password):
    if username in users and users[username] == hash_password(password):
        print("Login Successful")
    else:
        print("Invalid username or password")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        register(uname, pwd)

    elif choice == '2':
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        login(uname, pwd)

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
