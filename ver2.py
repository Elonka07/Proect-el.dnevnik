import json
from datetime import datetime, date
from random import choice

# Function to load data from diary from file
def load_diary(filename="school_diary.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Function to save diary data to a file
def save_diary(data, filename="school_diary.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# Function to add a new entry to the diary
def add_entry(diary):
    date = input("Enter the date (DD-MM-YYYY): ")
    if date not in diary:
        diary[date] = {"schedule": [], "homework": [], "notes": []}

    print("\n1. Add daily schedule")
    print("2. Add homework")
    print("3. Add notes")
    choice = input("Choose an option from 1 to 3: ")

    if choice == "1":
        event = input("Enter the schedule event(s) for this day (e.g. Math test from 8am): ")
        diary[date]["schedule"].append(event)
        print("Schedule updated.")
    elif choice == "2":
        homework = input("Enter the homework description: ")
        diary[date]["homework"].append(homework)
        print("Homework updated.")
    elif choice == "3":
        note = input("Enter the note: ")
        diary[date]["notes"].append(note)
        print("Note added.")
    else:
        print("Invalid choice.")


# Function to view entries for a specific date
def view_diary(diary):
    date = input("Enter the date (DD-MM-YYYY): ")

    if date in diary:
        print(f"\nDiary for {date}:")
        print("Schedule:")
        for i, event in enumerate(diary[date]["schedule"], 1):
            print(f"{i}. {event}")
        print("Homework:")
        for i, homework in enumerate(diary[date]["homework"], 1):
            print(f"{i}. {homework}")
        print("Notes:")
        for i, note in enumerate(diary[date]["notes"], 1):
            print(f"{i}. {note}")
    else:
        print("No entries for this date!")


# Function to delete an entry
def delete_entry(diary):
    date = input("Enter the date (DD-MM-YYYY): ")
    if date in diary:
        confirm = input(f"Are you sure you want to delete all entries for {date}? (yes/no): ")
        if confirm.lower() == "yes":
            del diary[date]
            print("Entries deleted.")
    else:
        print("Deletion canceled.")

# Main function
def main():
    diary = load_diary()
    while True:
        print("\n--School Diary--")
        print("1. Add Entry")
        print("2. View Entry")
        print("3. Delete Entry")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(diary)
        elif choice == "2":
            view_diary(diary)
        elif choice == "3":
            delete_entry(diary)
        elif choice == "4":
            save_diary(diary)
            print("Diary saved successfully.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
