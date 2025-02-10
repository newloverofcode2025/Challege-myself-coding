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

def calculate_angle_mbc(ab, bc):
    """
    Calculates the angle MBC in degrees.
    :param ab: Length of side AB
    :param bc: Length of side BC
    :return: The angle MBC in degrees
    """
    # Calculate AC using the Pythagorean theorem
    ac = math.sqrt(bc**2 - ab**2)

    # M is the midpoint of AC, so AM = MC = AC / 2
    mc = ac / 2

    # Use the tangent function to find ∠MBC
    angle_mbc_radians = math.atan(mc / ab)
    angle_mbc_degrees = math.degrees(angle_mbc_radians)

    return angle_mbc_degrees

if __name__ == "__main__":
    print("Welcome to the Angle MBC Calculator! 📐")

    # Get user input for side lengths
    ab = get_positive_float("Enter the length of side AB (opposite to the right angle): ")
    bc = get_positive_float("Enter the length of side BC (hypotenuse): ")

    # Validate that BC > AB (triangle inequality)
    if bc <= ab:
        print("Error: The hypotenuse (BC) must be greater than the other side (AB).")
    else:
        # Calculate the angle MBC
        angle_mbc = calculate_angle_mbc(ab, bc)

        # Display the result
        print(f"The angle MBC is: {angle_mbc:.2f}°")