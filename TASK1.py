users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def add_user(user_id, name, email):
    for user in users:
        if user["id"] == user_id:
            print("User ID already exists.")
            return
    users.append({"id": user_id, "name": name, "email": email})
    print("User added successfully.")

def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            print(user)
            return
    print("User not found.")

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated successfully.")
            return
    print("User not found.")

def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            print("User deleted successfully.")
            return
    print("User not found.")

# Menu for user input
while True:
    print("\n1. Add User")
    print("2. Get User by ID")
    print("3. Update User")
    print("4. Delete User")
    print("5. Show All Users")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        uid = int(input("Enter user ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        add_user(uid, name, email)

    elif choice == '2':
        uid = int(input("Enter user ID: "))
        get_user(uid)

    elif choice == '3':
        uid = int(input("Enter user ID: "))
        name = input("Enter new name (or press Enter to skip): ")
        email = input("Enter new email (or press Enter to skip): ")
        update_user(uid, name if name else None, email if email else None)

    elif choice == '4':
        uid = int(input("Enter user ID: "))
        delete_user(uid)

    elif choice == '5':
        for user in users:
            print(user)

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
