def get_number(prompt):
    """
    Prompts the user for a number and validates the input.
    :param prompt: The message to display to the user
    :return: A valid integer entered by the user
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

def calculate_sum_of_squares(n):
    """
    Calculates the sum of squares from 0^2 to n^2.
    :param n: The upper limit (inclusive)
    :return: The sum of squares
    """
    return sum(i**2 for i in range(n + 1))

if __name__ == "__main__":
    print("Welcome to the Sum of Squares Calculator! 🔢")

    # Get user input
    n = get_number("Enter a non-negative integer (n): ")

    # Calculate the sum of squares
    result = calculate_sum_of_squares(n)

    # Display the result
    print(f"The sum of squares from 0^2 to {n}^2 is: {result}")