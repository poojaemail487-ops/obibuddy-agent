from datetime import datetime

def daily_plan(prompt):
    return f"🗓 Your plan for today based on your prompt: {prompt}"

def task_manager(task, action):
    if action == "add":
        return f"✅ Task added: {task}"
    elif action == "remove":
        return f"❌ Task removed: {task}"
    else:
        return "Invalid action."

def habit_suggest():
    habits = [
        "Drink 2 glasses of water in the morning",
        "10-minute stretching",
        "Review your goals",
        "Write 3 gratitude notes",
        "Evening 5-min reflection"
    ]
    return habits

if __name__ == "__main__":
    print("ObiBuddy Agent Ready 🚀")
