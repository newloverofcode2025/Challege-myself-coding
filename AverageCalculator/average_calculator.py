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

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    :param numbers: List of numbers
    :return: The average of the numbers
    """
    if not numbers:
        return 0  # Handle the case where no numbers are entered
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Welcome to the Average Calculator! 🧮")

    numbers = []
    while True:
        # Get user input
        num = get_number("Enter a number (or type 'done' to finish): ")
        numbers.append(num)

        # Check if the user wants to stop entering numbers
        choice = input("Do you want to enter another number? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            break

    # Calculate and display the average
    average = calculate_average(numbers)
    print(f"The average of the entered numbers is: {average:.2f}")