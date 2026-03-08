import json
from system.logger import log_event

# Load brain memory
def load_memory():
    with open("data/brain_memory.json", "r") as file:
        return json.load(file)

# Save brain memory
def save_memory(data):
    with open("data/brain_memory.json", "w") as file:
        json.dump(data, file, indent=4)

# Emotion engine
def update_mood(data):
    mood = input("How are you feeling today? (happy/sad/neutral): ")
    data["mood"] = mood
    save_memory(data)

    log_event(f"Mood updated to {mood}")

    print("Mood updated successfully.\n")

# Progress engine
def record_task(data):
    answer = input("Did you complete a task today? (yes/no): ")

    if answer.lower() == "yes":
        data["tasks_completed"] += 1
        save_memory(data)

        log_event("Task completed")

        print("Great job! Task recorded.\n")
    else:
        print("No problem. Keep pushing forward.\n")

# Decision engine
def analyze_state(data):
    name = data["name"]
    mood = data["mood"]
    tasks = data["tasks_completed"]

    print("\nAnalyzing state for", name)
    print("Mood:", mood)
    print("Tasks Completed:", tasks)
    print()

    if mood == "sad" and tasks > 0:
        print("Even though you're feeling sad, you're still making progress.")
        print("That shows real discipline. Keep going.")

    elif mood == "happy" and tasks > 0:
        print("Great mood and steady progress.")
        print("Stay consistent and build momentum.")

    elif tasks == 0:
        print("No tasks completed yet.")
        print("Start small and build momentum.")

    else:
        print("Stay balanced and keep improving.")

    print("\nDecision analysis complete.\n")

    log_event("Decision analysis executed")

# Main controller
def main():

    data = load_memory()
    name = data["name"]

    while True:

        print("Welcome", name)
        print("1. Update Mood")
        print("2. Record Completed Task")
        print("3. Analyze Current State")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            update_mood(data)

        elif choice == "2":
            record_task(data)

        elif choice == "3":
            analyze_state(data)

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
