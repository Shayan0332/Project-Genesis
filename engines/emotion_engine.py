from system.logger import log_event

def update_mood(data, save_memory):

    mood = input("How are you feeling today? (happy/sad/neutral): ")

    data["mood"] = mood
    save_memory(data)

    log_event(f"Mood updated to {mood}")

    print("Mood updated successfully.\n")
