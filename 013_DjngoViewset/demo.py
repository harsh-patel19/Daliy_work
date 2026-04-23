import random

# Input from user
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

# Validation
if len(first_name) < 2 or len(last_name) < 2:
    print("Please enter at least 2 characters in both names.")
else:
    a = first_name[:2]
    b = last_name[-2:]

    random_number = random.randint(1000, 9999)

    password = a + b + str(random_number)

    print("Generated Password:", password)