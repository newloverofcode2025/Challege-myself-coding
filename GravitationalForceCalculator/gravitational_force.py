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

def calculate_gravitational_force(m1, m2, r):
    """
    Calculates the gravitational force between two objects.
    :param m1: Mass of the first object (in kg)
    :param m2: Mass of the second object (in kg)
    :param r: Distance between the centers of the two objects (in meters)
    :return: Gravitational force (in Newtons)
    """
    G = 6.674 * (10 ** -11)  # Gravitational constant
    return G * (m1 * m2) / (r ** 2)

if __name__ == "__main__":
    print("Welcome to the Gravitational Force Calculator! 🌍")

    # Get user input
    m1 = get_positive_float("Enter the mass of the first object (in kg): ")
    m2 = get_positive_float("Enter the mass of the second object (in kg): ")
    r = get_positive_float("Enter the distance between the objects (in meters): ")

    # Calculate gravitational force
    force = calculate_gravitational_force(m1, m2, r)

    # Display the result
    print(f"\nThe gravitational force between the objects is: {force:.2e} N")