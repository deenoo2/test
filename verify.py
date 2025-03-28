import re

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9]*$'
    if re.match(pattern, username):
        return True
    return False

# Example usage
username = input("Enter a username: ")
if validate_username(username):
    print("Valid username.")
else:
    print("Invalid username.")
    # Dinu - added next line
    print("Use only A-Z for the first character and A-z/0-9 for the name, no special characters are allowed.") 
