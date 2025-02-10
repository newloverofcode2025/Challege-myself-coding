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

def find_second_smallest(numbers):
    """
    Finds the second smallest number in a list.
    :param numbers: List of numbers
    :return: The second smallest number or None if not applicable
    """
    unique_numbers = sorted(set(numbers))  # Remove duplicates and sort
    if len(unique_numbers) < 2:
        return None  # Handle cases where there's no second smallest
    return unique_numbers[1]

if __name__ == "__main__":
    print("Welcome to the Second Smallest Element Finder! 🔢")

    numbers = []
    while True:
        # Get user input
        num = get_number("Enter a number (or type 'done' to finish): ")
        numbers.append(num)

        # Check if the user wants to stop entering numbers
        choice = input("Do you want to enter another number? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            break

    # Find the second smallest number
    second_smallest = find_second_smallest(numbers)
    if second_smallest is not None:
        print(f"The second smallest number in the list is: {second_smallest}")
    else:
        print("The list does not have enough unique numbers to determine the second smallest.")