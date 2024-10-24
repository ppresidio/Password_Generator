"""
Author: Pedro Presidio
Name: random_password_generator.py
Date: 28.9.2024
Update: 10/24/2024
Purpose: Generates a random password for the user
"""


import random
import string

# Function to generate the password
def generate_password(length, use_digits, use_uppercase, use_special):
    # Define character sets
    lower = string.ascii_lowercase
    digits = string.digits
    uppercase = string.ascii_uppercase
    special = string.punctuation

    # Ensure the password contains at least one character from each selected category
    char_pool = lower
    password = []

    if use_digits:
        password.append(random.choice(digits))
        char_pool += digits

    if use_uppercase:
        password.append(random.choice(uppercase))
        char_pool += uppercase

    if use_special:
        password.append(random.choice(special))
        char_pool += special

    # Fill the rest of the password with random characters from the selected pool
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Prompt the user for password length and preferences
def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"

    if not (use_digits or use_uppercase or use_special):
        print("You must include at least one of the following: digits, uppercase letters, or special characters.")
        return get_user_input()

    return length, use_digits, use_uppercase, use_special

# Save the password to a text file
def save_password_to_file(password):
    save = input("Would you like to save the password to a file? (yes/no): ").lower()
    if save == "yes":
        with open("password.txt", "w") as file:
            file.write(f"Your generated password is: {password}")
        print("Password saved to password.txt.")

# Main function
def main():
    length, use_digits, use_uppercase, use_special = get_user_input()
    password = generate_password(length, use_digits, use_uppercase, use_special)
    print(f"Your generated password is: {password}")
    save_password_to_file(password)

if __name__ == "__main__":
    main()
