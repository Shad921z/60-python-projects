# alarm-clock

# Import necessary modules
import time  # Provides time-related functions for sleep and current time
from datetime import datetime  # Provides functions to work with date and time

# Function to get the current time in HH:MM AM/PM format
def get_current_time():
    # Use datetime to get the current time and format it
    return datetime.now().strftime("%I:%M %p")

# Function to check and trigger the alarm
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")

    # Infinite loop to keep checking the time until the alarm time is reached
    while True:
        # Get the current time
        current_time = get_current_time()

        # Compare the current time with the alarm time
        if current_time == alarm_time:
            # Alarm notification
            print(f"Alarm! It's {alarm_time}. Time to wake up!")
            break  # Exit the loop after the alarm goes off

        # Sleep for 1 minute to avoid frequent checks
        time.sleep(60)

# Get the user input for the alarm time in HH:MM AM/PM format
alarm_time = input("Set alarm time (e.g., 07:30 AM): ")

# Set the alarm
set_alarm(alarm_time)
