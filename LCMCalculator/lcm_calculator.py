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

def lcm(a, b):
    """
    Calculates the least common multiple (LCM) of two numbers.
    :param a: First number
    :param b: Second number
    :return: The LCM of a and b
    """
    return abs(a * b) // math.gcd(a, b)

def calculate_lcm_of_list(numbers):
    """
    Calculates the LCM of a list of numbers.
    :param numbers: List of integers
    :return: The LCM of all numbers in the list
    """
    current_lcm = numbers[0]
    for num in numbers[1:]:
        current_lcm = lcm(current_lcm, num)
    return current_lcm

if __name__ == "__main__":
    print("Welcome to the Least Common Multiple (LCM) Calculator! 🔢")

    # Get the number of inputs
    n = get_positive_integer("How many numbers do you want to find the LCM for? ")

    # Get the numbers from the user
    numbers = []
    for i in range(n):
        num = get_positive_integer(f"Enter number {i + 1}: ")
        numbers.append(num)

    # Calculate the LCM
    result = calculate_lcm_of_list(numbers)

    # Display the result
    print(f"The LCM of {', '.join(map(str, numbers))} is: {result}")