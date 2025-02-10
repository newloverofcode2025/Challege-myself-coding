def get_temperature(prompt):
    """
    Prompts the user for a temperature and validates the input.
    :param prompt: The message to display to the user
    :return: A valid temperature entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    print("Welcome to the Temperature Converter! 🌡️")

    # Get user input
    celsius = get_temperature("Enter the temperature in Celsius: ")

    # Convert to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Display the result
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")