# day3_brain.py
# Project Genesis - Brain System (Memory Version 1)

# This program will:
# 1. Check if a memory file exists
# 2. If not, ask for user details
# 3. Save them
# 4. If yes, load memory and greet differently

import os  # This lets us check if a file exists

memory_file = "memory.txt"  # This is where we store data


# Function to save memory
def save_memory(name, age):
    # Open file in write mode ("w" means create or overwrite)
    with open(memory_file, "w") as file:
        file.write(name + "\n")  # Save name
        file.write(str(age))     # Save age


# Function to load memory
def load_memory():
    # Open file in read mode
    with open(memory_file, "r") as file:
        name = file.readline().strip()  # Read first line (name)
        age = file.readline().strip()   # Read second line (age)
    return name, age


# Main Brain Logic

# Check if memory file already exists
if os.path.exists(memory_file):
    # If yes, load existing memory
    name, age = load_memory()
    print("Welcome back,", name + "!")
    print("I remember you are", age, "years old.")
else:
    # If no memory found, ask user
    print("Hello, I don't know you yet.")
    name = input("What is your name? ")
    age = input("How old are you? ")
    # Make sure age is not empty
    while age.strip() == "":
       print("Age cannot be empty. Please enter your age.")
       age = input("How old are you? ")
    save_memory(name, age)

    print("Nice to meet you,", name + "!")
    print("I will remember you next time.")
