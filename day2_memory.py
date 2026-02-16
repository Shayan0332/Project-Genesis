# Project Genesis - Day 2: Simple Memory System

# File name where we store memory
filename = "memory.txt"

# Try to read existing memory
try:
    with open(filename, "r") as file:
        saved_name = file.read()
        print("Welcome back,", saved_name)
except:
    # If file does not exist, ask for name
    name = input("I don't know you yet. What is your name? ")
    
    # Save name to file
    with open(filename, "w") as file:
        file.write(name)
    
    print("Nice to meet you,", name)
