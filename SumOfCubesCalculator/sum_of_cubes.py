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

def calculate_sum_of_cubes_loop(n):
    """
    Calculates the sum of cubes using a loop.
    :param n: The upper limit (inclusive)
    :return: The sum of cubes
    """
    return sum(i**3 for i in range(1, n + 1))

def calculate_sum_of_cubes_formula(n):
    """
    Calculates the sum of cubes using the mathematical formula.
    :param n: The upper limit (inclusive)
    :return: The sum of cubes
    """
    return (n * (n + 1) // 2) ** 2

if __name__ == "__main__":
    print("Welcome to the Sum of Cubes Calculator! 🔢")

    # Get user input
    n = get_positive_integer("Enter a positive integer (n): ")

    # Calculate the sum of cubes using both methods
    sum_cubes_loop = calculate_sum_of_cubes_loop(n)
    sum_cubes_formula = calculate_sum_of_cubes_formula(n)

    # Display the results
    print(f"\nUsing Loop: The sum of cubes from 1 to {n} is: {sum_cubes_loop}")
    print(f"Using Formula: The sum of cubes from 1 to {n} is: {sum_cubes_formula}")