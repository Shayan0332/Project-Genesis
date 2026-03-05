import json
import os

BRAIN_FILE = "brain_memory.json"

# Load brain
if not os.path.exists(BRAIN_FILE):
    print("Brain memory not found. Run day3 first.")
    exit()

with open(BRAIN_FILE, "r") as file:
    brain = json.load(file)

print(f"Hello {brain['name']} ??")
print(f"Tasks completed so far: {brain['tasks_completed']}")

# Ask user
answer = input("Did you complete a task today? (yes/no): ").strip().lower()

if answer == "yes":
    brain["tasks_completed"] += 1
    print("Great job! Task recorded. ??")
elif answer == "no":
    print("No worries. Tomorrow is another opportunity.")
else:
    print("Invalid input. Please type yes or no.")
    exit()

# Intelligent response based on productivity
tasks = brain["tasks_completed"]

if tasks == 0:
    print("Let's start building momentum.")
elif 1 <= tasks <= 5:
    print("Good progress. Keep going!")
else:
    print("Excellent consistency! You're building discipline.")

# Save brain
with open(BRAIN_FILE, "w") as file:
    json.dump(brain, file, indent=4)

print(f"Total tasks completed: {brain['tasks_completed']}")
