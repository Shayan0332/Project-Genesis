def set_goal(data, save_memory):

    goal = input("What is your current goal? ")

    data["goal"] = goal

    save_memory(data)

    print("Goal saved successfully.\n")
