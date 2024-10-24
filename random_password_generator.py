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

