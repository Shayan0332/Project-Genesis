from system.logger import log_event

def analyze_state(data):

    print("\nAnalyzing state for", data["name"])
    print("Mood:", data["mood"])
    print("Tasks Completed:", data["tasks_completed"])
    print("Current Goal:", data["goal"])

    if data["goal"] != "":
        print("Working Toward:", data["goal"])

    # Score system
    score = 0

    # Mood scoring
    if data["mood"] == "happy":
        score += 2
    elif data["mood"] == "neutral":
        score += 1
    elif data["mood"] == "sad":
        score -= 1

    # Task scoring
    score += data["tasks_completed"]

    print("System Score:", score)
    print("Interactions:", data["interactions"])
    print("Mood Records:", len(data["mood_history"]))

    # Mood trend analysis
    if len(data["mood_history"]) >= 2:
        if data["mood_history"][-1] == "sad" and data["mood_history"][-2] == "sad":
            print("Mood Trend: You have been feeling sad recently.")

    # Intelligent response
    if score >= 3:
        print("\nExcellent state. You're performing very well.")
    elif score >= 1:
        print("\nGood progress. Stay consistent.")
    elif score == 0:
        print("\nBalanced state. Try to improve slightly.")
    else:
        print("\nLow state detected. Focus on small wins.")

    if data["interactions"] > 5:
        print("\nYou're consistently using the system. Great discipline.")

    if data["goal"] != "" and data["tasks_completed"] > 0:
        print("\nYou are making progress toward your goal.")

    if data["goal"] != "" and data["tasks_completed"] >= 5:
        print("\nOutstanding progress toward your goal!")

    if data["tasks_completed"] == 0:
        print("\nRecommendation: Complete one small task today.")

    if data["mood"] == "sad":
        print("\nRecommendation: Focus on one small win today.")

    print("\nDecision analysis complete.\n")

    log_event(f"Decision score calculated: {score}")
