# day3_brain_json.py
# Project Genesis - Brain System Version 2 (JSON MEMORY)
import os
import json # JSON allows structured data storage

memory_file = "brain_memory.json"

# Function to save memory
def save_memory(data):
    with open(memory_file, "w")as file:
        json.dump(data, file, indent=4) # Save dictionay in readable formate


# Function to load memory
def load_memory():
     with open(memory_file, "r") as file:
         data = json.load(file)  # Load JSON into dictionary 
     return data


# Main Brain Logic

if os.path.exists(memory_file):
    brain = load_memory()

    print("Welcome back,", brain["name"] + "!")
    print("I remember you are", brain["age"], "years old.")
    print("Your height is", brain["height"], "cm.")

else:
    print("Hello, I don't know you yet.")

    name = input("What is your name? ")
    while name.strip() == "":
        print("Name cannot be empty.")
        name = input("What is your name? ")

    age = input("How old are you? ")
    while not age.isdigit():
        print("Age must be a number.")
        age = input("How old are you? ")

    age = int(age)

    height = input("What is your height in cm? ")
    while True:
        try:
            height = float(height)
            break
        except ValueError:
            print("Height must be a number.")
            height = input("What is your height in cm? ")

    # Create structured brain dictionary 
    brain = {
        "name": name,
        "age": age,
        "height": height,
        "mood": "neutral",
        "tasks_completed": 0
    }

    save_memory(brain)

    print("Nice to meet you,", name + "!")
    print("Your data has been stored in my brain.")
