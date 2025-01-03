task = input("Enter task description: ")
task_priority = input("What is the priority of the task (High, Medium, Low): ").capitalize()
time_bound = input("Is the task time bound (Yes or No): ").strip().lower()

match task_priority:
    case "High":
        message = "It's a high priority task."
    case "Medium":
        message = "It's a medium priority task."
    case "Low":
        message = "It's a low priority task."
    case _:
        message = "Invalid priority specified."

print(message)

if time_bound == "yes":
    print(f"{task} is of {task_priority} priority and is time-bound.")
elif time_bound == "no":
    print(f"Note: {task} is of {task_priority} priority and is not time-bound.")
else:
    print("Invalid input for time-bound status.")
