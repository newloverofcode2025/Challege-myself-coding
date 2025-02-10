def get_positive_float(prompt):
    """
    Prompts the user for a positive float value and validates the input.
    :param prompt: The message to display to the user
    :return: A valid positive float entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_compound_interest(principal, rate, time, n):
    """
    Calculates the total amount and compound interest.
    :param principal: Principal amount (money borrowed or invested)
    :param rate: Annual interest rate (in decimal form)
    :param time: Time in years
    :param n: Number of times interest is compounded per year
    :return: Total amount and compound interest
    """
    total_amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = total_amount - principal
    return total_amount, compound_interest

if __name__ == "__main__":
    print("Welcome to the Compound Interest Calculator! 💰")

    # Get user input
    principal = get_positive_float("Enter the principal amount (money borrowed/invested): ")
    annual_rate = get_positive_float("Enter the annual interest rate (as a percentage, e.g., 5 for 5%): ") / 100
    time = get_positive_float("Enter the time period (in years): ")
    n = int(get_positive_float("Enter the number of times interest is compounded per year: "))

    # Calculate compound interest
    total_amount, compound_interest = calculate_compound_interest(principal, annual_rate, time, n)

    # Display the result
    print(f"\n--- Results ---")
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Annual Interest Rate: {annual_rate * 100:.2f}%")
    print(f"Time Period: {time} years")
    print(f"Compounding Frequency: {n} times per year")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Compound Interest: ${compound_interest:.2f}")