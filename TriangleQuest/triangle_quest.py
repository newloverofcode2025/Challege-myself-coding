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

def print_triangle(n):
    """
    Prints a numerical triangle pattern with n rows.
    :param n: Number of rows in the triangle
    """
    for i in range(1, n + 1):
        # Print the number 'i' repeated 'i' times
        print(str(i) * i)

if __name__ == "__main__":
    print("Welcome to the Triangle Quest! 🔺")

    # Get user input
    rows = get_positive_integer("Enter the number of rows for the triangle: ")

    # Print the triangle
    print("\nNumerical Triangle:")
    print_triangle(rows)