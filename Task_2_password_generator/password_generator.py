# Password Generator - Task 2

import string
import random

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 4): "))
    
    if length < 4:
        print("Password length should be at least 4!")
    else:
        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        characters = string.ascii_lowercase
        
        if include_upper:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += "!@#$%^&*"
        
        if not characters:
            print("No character sets selected!")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            print(f"\nGenerated Password: {password}")
            print(f"Password Strength: Strong" if length >= 8 else "Medium")

except ValueError:
    print("Please enter a valid number!")
    
