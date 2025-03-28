# - Dinu - validate the username

import re

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9]*$'
    return bool(re.match(pattern, username))

# Only run this part when the script is executed directly (not during import)
if __name__ == "__main__":
    username = input("Enter a username: ")
    if validate_username(username):
        print("Valid username.")
    else:
        print("Invalid username.")
        print("Use only A-Z for the first character and A-Z/0-9 for the name, no special characters are allowed")
