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

        # Mood statistics
    happy_count = data["mood_history"].count("happy")
    sad_count = data["mood_history"].count("sad")
    neutral_count = data["mood_history"].count("neutral")

    print("Mood Statistics:")
    print("Happy:", happy_count)
    print("Sad:", sad_count)
    print("Neutral:", neutral_count)

        # Most frequent mood
    mood_counts = {
        "happy": happy_count,
        "sad": sad_count,
        "neutral": neutral_count
    }

    most_frequent_mood = max(mood_counts, key=mood_counts.get)

    print("Most Frequent Mood:", most_frequent_mood)

    if len(data["task_history"]) > 0:
        print("Latest Task:", data["task_history"][-1])

        # Productivity statistics
    print("Task Records:", len(data["task_history"]))
    print("Goals Completed:", len(data["completed_goals"]))

        # Productivity insight
    if data["tasks_completed"] >= 5:
        print("Productivity Insight: You are maintaining strong task completion.")

    if len(data["completed_goals"]) >= 2:
        print("Achievement Insight: You have completed multiple goals.")

    if len(data["completed_goals"]) > 0:
        print("Latest Achievement:", data["completed_goals"][-1])

        # Overall personal insight
    if data["mood"] == "sad" and data["tasks_completed"] >= 5:
        print("Overall Insight: Despite your mood, you are continuing to make strong progress.")

    elif data["mood"] == "happy" and data["tasks_completed"] >= 5:
        print("Overall Insight: Your positive mood is supporting strong productivity.")

    elif data["tasks_completed"] >= 5:
        print("Overall Insight: You are maintaining consistent productivity.")

    else:
        print("Overall Insight: Focus on steady progress and small improvements.")

    # Recent activity
    if len(data["activity_log"]) > 0:
        print("Recent Activity:")

        for activity in data["activity_log"][-3:]:
            print("-", activity)

    # Mood trend analysis
    if len(data["mood_history"]) >= 2:
        if (
            data["mood_history"][-1] == "sad"
            and data["mood_history"][-2] == "sad"
        ):
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

    # Interaction analysis
    if data["interactions"] > 5:
        print("\nYou're consistently using the system. Great discipline.")

    # Goal progress analysis
    if data["goal"] != "" and data["tasks_completed"] > 0:
        print("\nYou are making progress toward your goal.")

    if data["goal"] != "" and data["tasks_completed"] >= 5:
        print("\nOutstanding progress toward your goal!")

    # Recommendations
    if data["tasks_completed"] == 0:
        print("\nRecommendation: Complete one small task today.")

    if data["mood"] == "sad":
        print("\nRecommendation: Focus on one small win today.")

    print("\nDecision analysis complete.\n")

    log_event(f"Decision score calculated: {score}")
