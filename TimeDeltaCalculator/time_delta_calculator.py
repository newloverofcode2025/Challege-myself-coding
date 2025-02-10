from datetime import datetime

def get_timestamp(prompt):
    """
    Prompts the user for a timestamp in the format YYYY-MM-DD HH:MM:SS and validates the input.
    :param prompt: The message to display to the user
    :return: A valid datetime object entered by the user
    """
    while True:
        try:
            timestamp_str = input(prompt)
            return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid input. Please enter the timestamp in the format YYYY-MM-DD HH:MM:SS.")

def calculate_time_delta(start, end):
    """
    Calculates the time difference (delta) between two timestamps.
    :param start: The start timestamp
    :param end: The end timestamp
    :return: A timedelta object representing the difference
    """
    return end - start

if __name__ == "__main__":
    print("Welcome to the Time Delta Calculator! ⏳")

    # Get user input for the first timestamp
    print("\nEnter the start timestamp:")
    start_time = get_timestamp("Start (YYYY-MM-DD HH:MM:SS): ")

    # Get user input for the second timestamp
    print("\nEnter the end timestamp:")
    end_time = get_timestamp("End (YYYY-MM-DD HH:MM:SS): ")

    # Ensure the start time is earlier than the end time
    if start_time > end_time:
        print("The start timestamp must be earlier than the end timestamp. Swapping timestamps.")
        start_time, end_time = end_time, start_time

    # Calculate the time delta
    delta = calculate_time_delta(start_time, end_time)

    # Display the result
    print(f"\nThe time difference between {start_time} and {end_time} is:")
    print(f"{delta.days} days, {delta.seconds // 3600} hours, {(delta.seconds % 3600) // 60} minutes, and {delta.seconds % 60} seconds.")