import json
import os

BRAIN_FILE = "brain_memory.json"

# Check if brain exists
if not os.path.exists(BRAIN_FILE):
    print("Brain memory not found. Run setup first.")
    exit()

# Load brain
with open(BRAIN_FILE, "r") as file:
    brain = json.load(file)

name = brain["name"]
mood = brain["mood"]
tasks = brain["tasks_completed"]

print(f"\nAnalyzing state for {name}...")
print(f"Mood: {mood}")
print(f"Tasks Completed: {tasks}\n")

# Decision Logic (Fusion of Mood + Productivity)

if mood == "sad" and tasks == 0:
    print("You're feeling low and haven't started yet.")
    print("Start small. One task can change your momentum.")

elif mood == "sad" and tasks > 0:
    print("Even though you're feeling sad, you're still making progress.")
    print("That shows real discipline. Keep going.")

elif mood == "happy" and tasks > 5:
    print("You're happy and highly productive!")
    print("You're operating at peak performance. Excellent work.")

elif mood == "happy" and tasks <= 5:
    print("Great mood and steady progress.")
    print("Stay consistent and build momentum.")

elif mood == "neutral":
    print("Stable mindset detected.")
    print("Consistency will determine your growth.")

else:
    print("State unclear, but keep pushing forward.")

print("\nDecision analysis complete.")
