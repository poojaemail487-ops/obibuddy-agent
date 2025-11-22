# ObiBuddy Core System

from datetime import datetime

def plan_day(user_input):
    return {
        "date": str(datetime.now().date()),
        "plan": f"Your plan based on your input: {user_input}"
    }

def add_task(task):
    return f"Task added: {task}"

def remove_task(task):
    return f"Task removed: {task}"

def habit_suggestions():
    habits = [
        "Morning deep breathing for 2 mins",
        "Drink 2 glasses of water",
        "10-min focus work",
        "Evening reflection journal",
        "Night digital detox for 30 mins"
    ]
    return habits

print("ObiBuddy Core Loaded ✔")
