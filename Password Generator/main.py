#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_password = ""
password_list = []
count = 0
for char in password:
    password_list.insert(count, char)
    count += 1;
total_chars = nr_letters + nr_numbers + nr_symbols;

while len(new_password) != total_chars:
    choice = random.choice(password_list)
    index = password_list.index(choice)
    new_password += choice
    password_list.pop(index)

print(new_password)

# ChatGPT's code:
# import random

# def generate_password(nr_letters, nr_symbols, nr_numbers):
#     letters = [
#         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#         'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#         'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#         'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
#     ]
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password = []
    
#     password.extend(random.choices(letters, k=nr_letters))
#     password.extend(random.choices(symbols, k=nr_symbols))
#     password.extend(random.choices(numbers, k=nr_numbers))

#     random.shuffle(password)
    
#     return ''.join(password)

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# new_password = generate_password(nr_letters, nr_symbols, nr_numbers)
# print(new_password)
