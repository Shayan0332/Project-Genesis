# day4_emotion_engine.py
# Project Genesis - Emotion Engine Layer

import json
import os

memory_file = "brain_memory.json"

def load_brain():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            return json.load(file)
    return None


def save_brain(brain):
    with open(memory_file, "w") as file:
        json.dump(brain, file, indent=4)


def emotional_response(brain):
    mood = brain["mood"]

    if mood == "happy":
        print("Great to see you again,", brain["name"] + "! ??")
    elif mood == "sad":
        print("I hope your day gets better,", brain["name"] + ".")
    else:
        print("Welcome back,", brain["name"] + ".")

def update_mood(brain):
    new_mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

    if new_mood in ["happy", "sad", "neutral"]:
        brain["mood"] = new_mood
        save_brain(brain)
        print("Mood updated successfully.")
    else:
        print("Invalid mood. Keeping previous mood.")


# Main execution

brain = load_brain()

if brain:
    emotional_response(brain)
    update_mood(brain)
else:
    print("Brain memory not found. Please run day3_brain_json.py first.")

