 #daily_reminder.py

# Step 1: Ask user for task description
task = input("Enter your task: ")

# Step 2: Ask user for priority level
priority = input("Priority (high/medium/low): ").lower()

# Step 3: Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 4: Process task and provide reminder based on priority and time sensitivity

# Use match-case for priority
match priority:
    case 'high':
        priority_message = "high priority task"
    case 'medium':
        priority_message = "medium priority task"
    case 'low':
        priority_message = "low priority task"
    case _:
        priority_message = "unknown priority level"

# If the task is time-bound, modify the reminder message
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."

# Step 5: Output the reminder message
print(f"Reminder: {reminder}")  # This is the line that should be checke
