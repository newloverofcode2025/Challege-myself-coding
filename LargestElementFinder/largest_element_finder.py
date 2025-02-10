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

def find_largest(numbers):
    """
    Finds the largest number in a list.
    :param numbers: List of numbers
    :return: The largest number
    """
    if not numbers:
        return None  # Handle the case where the list is empty
    return max(numbers)

if __name__ == "__main__":
    print("Welcome to the Largest Element Finder! 🏆")

    numbers = []
    while True:
        # Get user input
        num = get_number("Enter a number (or type 'done' to finish): ")
        numbers.append(num)

        # Check if the user wants to stop entering numbers
        choice = input("Do you want to enter another number? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            break

    # Find and display the largest number
    largest = find_largest(numbers)
    if largest is not None:
        print(f"The largest number in the list is: {largest}")
    else:
        print("No numbers were entered.")