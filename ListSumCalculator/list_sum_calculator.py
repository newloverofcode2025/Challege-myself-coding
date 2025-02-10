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

def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.
    :param numbers: List of numbers
    :return: The sum of the numbers
    """
    return sum(numbers)

if __name__ == "__main__":
    print("Welcome to the List Sum Calculator! 🧮")

    numbers = []
    while True:
        # Get user input
        num = get_number("Enter a number (or type 'done' to finish): ")
        numbers.append(num)

        # Check if the user wants to stop entering numbers
        choice = input("Do you want to enter another number? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            break

    # Calculate and display the sum
    total = calculate_sum(numbers)
    print(f"The sum of the entered numbers is: {total}")