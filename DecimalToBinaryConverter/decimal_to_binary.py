def decimal_to_binary_recursive(n):
    """
    Converts a decimal number to binary using recursion.
    :param n: The decimal number to convert
    :return: Binary representation as a string
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2)

def get_number(prompt):
    """
    Prompts the user for a number and validates the input.
    :param prompt: The message to display to the user
    :return: A valid non-negative integer entered by the user
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

if __name__ == "__main__":
    print("Welcome to the Decimal to Binary Converter! 🔢")

    # Get user input
    decimal_number = get_number("Enter a non-negative decimal number: ")

    # Convert to binary using recursion
    binary_representation = decimal_to_binary_recursive(decimal_number)

    # Display the result
    print(f"The binary representation of {decimal_number} is: {binary_representation}")