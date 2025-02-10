import math

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

def euclidean_gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two numbers using the Euclidean Algorithm.
    :param a: First number
    :param b: Second number
    :return: The GCD of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("Welcome to the Greatest Common Divisor (GCD) Calculator! 🔢")

    # Get user input
    num1 = get_positive_integer("Enter the first number: ")
    num2 = get_positive_integer("Enter the second number: ")

    # Calculate GCD using the built-in method
    gcd_builtin = math.gcd(num1, num2)

    # Calculate GCD using the Euclidean Algorithm
    gcd_euclidean = euclidean_gcd(num1, num2)

    # Display the results
    print(f"\nUsing Built-in Method: The GCD of {num1} and {num2} is: {gcd_builtin}")
    print(f"Using Euclidean Algorithm: The GCD of {num1} and {num2} is: {gcd_euclidean}")