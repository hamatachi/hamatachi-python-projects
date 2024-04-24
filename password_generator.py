#Password Generator Project

author = "Hamatachi"

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = len(letters) + len(symbols) + len(numbers)
total_letters = len(letters)
total_symbols = len(symbols)
total_numbers = len(numbers)

user_total = nr_letters + nr_symbols + nr_numbers

user_password = ""

for letters_password in range(0, nr_letters):
    user_password += letters[random.randint(0, (total_letters - 1))]

for symbols_password in range(0, nr_symbols):
    user_password += symbols[random.randint(0, (total_symbols - 1))]

for numbers_password in range(0, nr_numbers):
    user_password += numbers[random.randint(0, (total_numbers - 1))]

encryption = list(user_password)

random.shuffle(encryption)

password_strong = "".join(encryption)

print(f"Your generated password is {password_strong}")

