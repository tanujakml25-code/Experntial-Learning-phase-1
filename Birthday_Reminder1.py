# Birthday Reminder - 20% Initial Code

birthdays = {}

def add_birthday():
    name = input("Enter person's name: ")
    birthday = input("Enter birthday (DD-MM-YYYY): ")

    birthdays[name] = birthday

    print("Birthday added successfully!")


def search_birthday():
    name = input("Enter name to search: ")

    if name in birthdays:
        print("Birthday:", birthdays[name])
    else:
        print("Birthday record not found.")


# Main Menu
while True:
    print("\n===== BIRTHDAY REMINDER =====")
    print("1. Add Birthday")
    print("2. Search Birthday")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_birthday()

    elif choice == "2":
        search_birthday()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
