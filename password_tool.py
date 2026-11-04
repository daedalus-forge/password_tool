# IMPORTS
import secrets
import string
from getpass import getpass

# CONSTANTS
CHARACTERS = string.ascii_letters + string.digits + string.punctuation


# FUNCTIONS
def get_length():
    while True:
        try:
            length = int(input("How long should the password be? "))
        except ValueError:
            print(
                "That is not a valid number. Please enter a whole number between 8 and 64."
            )
            continue

        if length < 8:
            print(
                f"{length} is too short. Password must be between 8 and 64 characters long."
            )
        elif length > 64:
            print(
                f"{length} is too long. Password must be between 8 and 64 characters long."
            )
        else:
            return length


def generate_password(length):
    password = ""
    for _ in range(length):
        password += secrets.choice(CHARACTERS)
    return password


def check_strength(password):
    score = 0

    # Length Checks
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    # Complexity Check
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True

    # Add points for flags
    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_symbol:
        score += 1

    # Score = Rating
    if score <= 3:
        rating = "Weak"
    elif score <= 5:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, score


def show_strength(password):
    # get rating and score from check_strength
    # print them in one line like 'Rating: Strong (6/7)'
    rating, score = check_strength(password)
    print(f"Rating: {rating} ({score}/7)")


def load_common_passwords():
    common_passwords = []
    with open("common_passwords.txt") as file:
        for line in file:
            common_passwords.append(line.strip().lower())

    return common_passwords


def main():
    common_passwords = load_common_passwords()
    while True:
        print("\n===Password Tool===")
        print("1. Generate a password")
        print("2. Check password strength")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            # Generate a password
            length = get_length()
            password = generate_password(length)
            print(f"Password: {password}")
            show_strength(password)
        elif choice == "2":
            # Check a password
            password = getpass("Enter a password to check: ")
            show_strength(password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from options 1, 2 or 3")


main()
