import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    print("Welcome to the Password Generator application!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4 characters): "))
            if length < 4:
                print("Password should be at least 4 characters long. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    password_generator()
