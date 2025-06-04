task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match time_bound:
    case "yes":
        message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        print(message)
    case "no":
        message = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
        print(message)
