from system.logger import log_event


def generate_summary(data):

    print("\n========== DAILY SUMMARY ==========")

    print("Name:", data["name"])
    print("Current Mood:", data["mood"])
    print("Tasks Completed:", data["tasks_completed"])
    print("Goals Completed:", len(data["completed_goals"]))

    if data["goal"] != "":
        print("Current Goal:", data["goal"])
    else:
        print("Current Goal: None")

    if len(data["mood_history"]) > 0:
        mood_counts = {
            "happy": data["mood_history"].count("happy"),
            "sad": data["mood_history"].count("sad"),
            "neutral": data["mood_history"].count("neutral")
        }

        most_frequent_mood = max(
            mood_counts,
            key=mood_counts.get
        )

        print("Most Frequent Mood:", most_frequent_mood)

    if len(data["task_history"]) > 0:
        print("Latest Task:", data["task_history"][-1])

    if len(data["completed_goals"]) > 0:
        print("Latest Achievement:", data["completed_goals"][-1])

    if len(data["activity_log"]) > 0:
        print("\nRecent Activity:")

        for activity in data["activity_log"][-3:]:
            print("-", activity)

    print("\n========== END SUMMARY ==========\n")

    log_event("Daily summary generated")
