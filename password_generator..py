import string
import random

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("No character sets selected for password generation.")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    length = int(input("Enter desired password length: "))
    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
    strong_password = generate_password(length, include_upper, include_digits, include_symbols)
    print("\nGenerated Password:", strong_password)

except ValueError:
    print("Invalid input. Please enter a valid number for length.")
