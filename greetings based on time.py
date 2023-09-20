import time

# Get the current time in the format HH:MM:SS
timestamp = time.strftime('%H:%M:%S')

# Extract the hours from the timestamp
n = int(timestamp[0:2])

# Determine the time of day
if n < 6:
    print("Good Night")
elif n < 12:
    print("Good Morning")
elif n < 18:
    print("Good Afternoon")
else:
    print("Good Evening")
