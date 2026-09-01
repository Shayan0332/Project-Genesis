from system.logger import log_event


def set_goal(data, save_memory):

    goal = input("What is your current goal? ")

    data["goal"] = goal

    save_memory(data)

    print("Goal saved successfully.\n")


def complete_goal(data, save_memory):

    if data["goal"] == "":
        print("No active goal found.\n")
        return

    data["completed_goals"].append(data["goal"])

    data["activity_log"].append(
        f"Goal completed: {data['goal']}"
    )

    print("Goal completed:", data["goal"])

    data["goal"] = ""

    save_memory(data)

    print("Goal completion recorded.\n")
