import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation


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
    for i in range(length):
        password += secrets.choice(characters)
    return password


length = get_length()
password = generate_password(length)
print(f"Your {length}-character password is: {password}")
