from system.logger import log_event

def analyze_state(data):

    print("\nAnalyzing state for", data["name"])
    print("Mood:", data["mood"])
    print("Tasks Completed:", data["tasks_completed"])

    if data["mood"] == "sad" and data["tasks_completed"] > 0:
        print("\nEven though you're feeling sad, you're still making progress.")
        print("That shows real discipline. Keep going.")

    elif data["mood"] == "happy" and data["tasks_completed"] > 0:
        print("\nGreat mood and steady progress.")
        print("Stay consistent and build momentum.")

    elif data["tasks_completed"] == 0:
        print("\nNo progress yet.")
        print("Start with small steps today.")

    else:
        print("\nStay consistent. You're doing okay.")

    print("\nDecision analysis complete.\n")

    log_event("Decision analysis executed")
