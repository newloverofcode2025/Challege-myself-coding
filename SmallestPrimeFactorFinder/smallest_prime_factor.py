def get_positive_integer(prompt):
    """
    Prompts the user for a positive integer and validates the input.
    :param prompt: The message to display to the user
    :return: A valid positive integer entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 1:
                print("Please enter an integer greater than 1.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def is_prime(n):
    """
    Checks if a number is prime.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_smallest_prime_factor(n):
    """
    Finds the smallest prime factor of a number.
    :param n: The number to analyze
    :return: The smallest prime factor of the number
    """
    if n % 2 == 0:
        return 2  # 2 is the smallest prime number
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            return factor
        factor += 2  # Increment by 2 to check only odd numbers
    return n  # If no factor is found, the number itself is prime

if __name__ == "__main__":
    print("Welcome to the Smallest Prime Factor Finder! 🔢")

    # Get user input
    number = get_positive_integer("Enter a number greater than 1: ")

    # Find the smallest prime factor
    smallest_prime = find_smallest_prime_factor(number)

    # Display the result
    print(f"The smallest prime factor of {number} is: {smallest_prime}")