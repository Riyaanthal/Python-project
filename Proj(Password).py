import random
import string

def generate_password(length=12):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

# Example usage
password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))