import math

def get_positive_float(prompt):
    """
    Prompts the user for a positive float value and validates the input.
    :param prompt: The message to display to the user
    :return: A valid positive float entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def is_valid_triangle(a, b, c):
    """
    Checks if the given sides form a valid triangle.
    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :return: True if the sides form a valid triangle, False otherwise
    """
    return a + b > c and a + c > b and b + c > a

def calculate_triangle_area(a, b, c):
    """
    Calculates the area of a triangle using Heron's Formula.
    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :return: The area of the triangle
    """
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's Formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

if __name__ == "__main__":
    print("Welcome to the Triangle Area Calculator! 📐")

    # Get user input
    a = get_positive_float("Enter the length of side a: ")
    b = get_positive_float("Enter the length of side b: ")
    c = get_positive_float("Enter the length of side c: ")

    # Check if the sides form a valid triangle
    if not is_valid_triangle(a, b, c):
        print("Error: The given sides do not form a valid triangle.")
    else:
        # Calculate the area
        area = calculate_triangle_area(a, b, c)

        # Display the result
        print(f"The area of the triangle is: {area:.2f}")