
import random
import string


def get_random_lowercase():
    return random.choice(string.ascii_lowercase)

def get_random_uppercase():
    return random.choice(string.ascii_uppercase)

def get_random_digit():
    return random.choice(string.digits)

def get_random_symbol():
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    return random.choice(symbols)

class PasswordGenerator:
    def __init__(self, length=8, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def generate(self):
        char_pool = ""
        if self.use_lower:
            char_pool += string.ascii_lowercase
        if self.use_upper:
            char_pool += string.ascii_uppercase
        if self.use_digits:
            char_pool += string.digits
        if self.use_symbols:
            char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        if not char_pool:
            return "Error: No character sets selected."

        return "".join(random.choice(char_pool) for _ in range(self.length))



def ask_length():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length > 0:
                return length
            else:
                print("Length must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_yes_no(prompt):
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"

# -------------------------------
# Main Program
# -------------------------------

def main():
    print("🔑 Password Generator 🔑")

    length = ask_length()
    use_lower = ask_yes_no("Include lowercase letters?")
    use_upper = ask_yes_no("Include uppercase letters?")
    use_digits = ask_yes_no("Include digits?")
    use_symbols = ask_yes_no("Include symbols?")

    generator = PasswordGenerator(length, use_lower, use_upper, use_digits, use_symbols)
    password = generator.generate()

    print("\nGenerated Password:", password)
    print("Strength:", password_strength(password))

if __name__ == "__main__":
    main()
