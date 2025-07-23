#Password Generator Project
import random
# Lists of available characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get user input for password composition
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Create an empty list to store the selected characters
password_list = []

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list to randomize character order
random.shuffle(password_list)

# Join the list into a single password string
password = "".join(password_list)

# Display the generated password
print(f"Your password is: {password}")