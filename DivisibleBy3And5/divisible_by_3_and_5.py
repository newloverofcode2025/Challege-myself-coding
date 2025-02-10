def get_number(prompt):
    """
    Prompts the user for a number and validates the input.
    :param prompt: The message to display to the user
    :return: A valid number entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def find_divisible_numbers(limit):
    """
    Finds all numbers smaller than the given limit that are divisible by both 3 and 5.
    :param limit: The upper limit (exclusive)
    :return: List of numbers divisible by both 3 and 5
    """
    divisible_numbers = [num for num in range(1, limit) if num % 3 == 0 and num % 5 == 0]
    return divisible_numbers

if __name__ == "__main__":
    print("Welcome to the Divisible by 3 and 5 Finder! 🔢")

    # Get user input
    limit = get_number("Enter a number: ")

    # Find numbers divisible by both 3 and 5
    divisible_numbers = find_divisible_numbers(limit)

    # Display the result
    if divisible_numbers:
        print(f"Numbers smaller than {limit} divisible by both 3 and 5:")
        print(", ".join(map(str, divisible_numbers)))
    else:
        print(f"No numbers smaller than {limit} are divisible by both 3 and 5.")