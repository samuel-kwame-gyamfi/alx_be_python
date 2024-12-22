# Prompt for task description
task = input("Enter the task description: ")

# Prompt for task priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority. Please recheck."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Provide a customized reminder
print(reminder)

