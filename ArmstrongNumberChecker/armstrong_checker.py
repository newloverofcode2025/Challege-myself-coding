def get_positive_integer(prompt):
    """
    Prompts the user for a positive integer and validates the input.
    :param prompt: The message to display to the user
    :return: A valid positive integer entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_armstrong_number(number):
    """
    Checks whether a number is an Armstrong number.
    :param number: The number to check
    :return: True if the number is an Armstrong number, False otherwise
    """
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number

if __name__ == "__main__":
    print("Welcome to the Armstrong Number Checker! 🔢")

    # Get user input
    number = get_positive_integer("Enter a non-negative integer to check: ")

    # Check if the number is an Armstrong number
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number!")
    else:
        print(f"{number} is not an Armstrong number.")