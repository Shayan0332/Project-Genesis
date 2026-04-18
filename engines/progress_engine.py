from system.logger import log_event

def record_task(data, save_memory):

    print("Tasks completed so far:", data["tasks_completed"])

    answer = input("Did you complete a task today? (yes/no): ")

    if answer.lower() == "yes":	
        data["tasks_completed"] += 1
        save_memory(data)

        log_event("Task completed")

        print("Great job! Task recorded.\n")

    else:
        print("No worries. Tomorrow is another opportunity.\n")
