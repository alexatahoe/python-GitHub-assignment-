# Welcome message 
print("Welcome to my Python program!")

# Ask user for study hours 
hours = input("How many hours did you study today?")

# Convert input to float with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

#Calculate weekly study hours 
weekly_hours = hours * 7

#Display result
print(f"You are on track to study {weekly_hours} hours this week.")