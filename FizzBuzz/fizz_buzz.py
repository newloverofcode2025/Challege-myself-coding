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

def fizz_buzz(n):
    """
    Generates the FizzBuzz sequence from 1 to n.
    :param n: The upper limit of the sequence
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    print("Welcome to the FizzBuzz Challenge! 🎉")

    # Get the upper limit from the user
    n = get_positive_integer("Enter the upper limit for FizzBuzz: ")

    # Generate and display the FizzBuzz sequence
    print("\nFizzBuzz Sequence:")
    fizz_buzz(n)