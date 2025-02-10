def get_positive_integer(prompt):
    """
    Prompts the user for a positive integer and validates the input.
    :param prompt: The message to display to the user
    :return: A valid positive integer entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_leap_year(year):
    """
    Determines whether a given year is a leap year.
    :param year: The year to check
    :return: True if the year is a leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if __name__ == "__main__":
    print("Welcome to the Leap Year Checker! 📅")

    # Get user input
    year = get_positive_integer("Enter a year to check: ")

    # Check if the year is a leap year
    result = is_leap_year(year)

    # Display the result
    if result:
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")