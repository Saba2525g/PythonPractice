import random
import string

print("PASSWORD GENERATOR")
print("=" * 30)

length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

password = "".join(random.choice(characters) for _ in range(length))
print(f"your password: {password}")

strength = "weak"
if length >= 8 and use_numbers and use_symbols:
    strength = "strong"
elif length >= 6 and (use_numbers or use_symbols):
    strength = "medium"

print(f"strength: {strength}")