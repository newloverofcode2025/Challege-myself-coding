def get_number(prompt):
    """
    Prompts the user for a number and validates the input.
    :param prompt: The message to display to the user
    :return: A valid number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def find_largest(num1, num2, num3):
    """
    Finds the largest of three numbers.
    :param num1: First number
    :param num2: Second number
    :param num3: Third number
    :return: The largest number
    """
    return max(num1, num2, num3)

if __name__ == "__main__":
    print("Welcome to the Largest Number Finder! 🏆")

    # Get user input
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    num3 = get_number("Enter the third number: ")

    # Find the largest number
    largest = find_largest(num1, num2, num3)
    print(f"The largest number is: {largest}")