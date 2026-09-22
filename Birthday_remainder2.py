from datetime import datetime
import json
import os

FILE_NAME = "birthdays.json"


# Load birthday records
def load_birthdays():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error loading birthday records.")
            return {}
    return {}


# Save birthday records
def save_birthdays(birthdays):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(birthdays, file, indent=4)
    except OSError:
        print("Error saving birthday records.")


# Validate birthday date
def is_valid_date(birthday):
    try:
        datetime.strptime(birthday, "%d-%m-%Y")
        return True
    except ValueError:
        return False


# Add birthday
def add_birthday(birthdays):
    name = input("Enter name: ").strip()
    birthday = input("Enter birthday (DD-MM-YYYY): ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    if not is_valid_date(birthday):
        print("Invalid date! Please use DD-MM-YYYY format.")
        return

    birthdays[name] = birthday
    save_birthdays(birthdays)
    print("Birthday added successfully!")


# Update birthday
def update_birthday(birthdays):
    name = input("Enter name to update: ").strip()

    if name in birthdays:
        new_birthday = input("Enter new birthday (DD-MM-YYYY): ").strip()

        if not is_valid_date(new_birthday):
            print("Invalid date! Please use DD-MM-YYYY format.")
            return

        birthdays[name] = new_birthday
        save_birthdays(birthdays)
        print("Birthday updated successfully!")

    else:
        print("Person not found!")


# Search birthday
def search_birthday(birthdays):
    name = input("Enter name to search: ").strip()

    if name in birthdays:
        print(name + "'s birthday is", birthdays[name])
    else:
        print("Person not found!")


# Delete birthday
def delete_birthday(birthdays):
    name = input("Enter name to delete: ").strip()

    if name in birthdays:
        del birthdays[name]
        save_birthdays(birthdays)
        print("Birthday deleted successfully!")
    else:
        print("Person not found!")


# Birthday notification
def notify_birthdays(birthdays):
    today = datetime.today()
    found = False

    for name, birthday in birthdays.items():
        birthday_date = datetime.strptime(birthday, "%d-%m-%Y")

        if birthday_date.day == today.day and birthday_date.month == today.month:
            print("Today is " + name + "'s birthday! 🎉")
            found = True

        elif birthday_date.month == today.month:
            print(name + "'s birthday is coming this month! 🔔")
            found = True

    if not found:
        print("No upcoming birthdays this month.")


# Show all birthdays
def show_all_birthdays(birthdays):
    if birthdays:
        print("\nAll Birthday Records:")
        for name, birthday in birthdays.items():
            print(name, "-", birthday)
    else:
        print("No birthday records found.")


# Main program
birthdays = load_birthdays()

while True:

    print("\n===== BIRTHDAY REMINDER =====")
    print("1. Add Birthday")
    print("2. Update Birthday")
    print("3. Search Birthday")
    print("4. Delete Birthday")
    print("5. Birthday Notification")
    print("6. Show All Birthdays")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_birthday(birthdays)

    elif choice == "2":
        update_birthday(birthdays)

    elif choice == "3":
        search_birthday(birthdays)

    elif choice == "4":
        delete_birthday(birthdays)

    elif choice == "5":
        notify_birthdays(birthdays)

    elif choice == "6":
        show_all_birthdays(birthdays)

    elif choice == "7":
        print("Thank you for using Birthday Reminder!")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")