from brain.memory_manager import load_memory, save_memory
from engines.emotion_engine import update_mood
from engines.progress_engine import record_task
from engines.decision_engine import analyze_state
from engines.goal_engine import set_goal, complete_goal

def main():

    data = load_memory()

    if not data:
        print("No memory found. Please initialize system first.")
        return

    while True:

        data["interactions"] += 1
        save_memory(data)
        print("\nWelcome", data["name"])
        print("1. Update Mood")
        print("2. Record Completed Task")
        print("3. Analyze Current State")
        print("4. Set Goal")
        print("5. Complete Goal")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            update_mood(data, save_memory)

        elif choice == "2":
            record_task(data, save_memory)

        elif choice == "3":
            analyze_state(data)

        elif choice == "4":
            set_goal(data, save_memory)

        elif choice == "5":
            complete_goal(data, save_memory)

        elif choice == "6":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
