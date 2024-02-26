from database import add_entry, get_entries, create_table
import sqlite3

menu = '''Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your Selection: '''

welcome = "Welcome to the programming diary"

def prompt_new_entry():
    # Take entry inputs
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    # Add to Python list as dictionaries (To simulate a primitive database.)
    add_entry(entry_content, entry_date)

def view_entries(entries):
    # get entries from entries list in database.py
    get_entries()
    # loop through entries to format for easier readability
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

print(welcome)

create_table()

while (user_input := input(menu)) != '3':
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_entries(get_entries())
    else:
        print('Invalid option, please choose a listed option.')
