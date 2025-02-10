def get_credit_card_number():
    """
    Prompts the user for a credit card number and validates the input.
    :return: A valid credit card number as a string
    """
    while True:
        card_number = input("Enter a credit card number (digits only): ").strip()
        if card_number.isdigit() and len(card_number) >= 12 and len(card_number) <= 19:
            return card_number
        print("Invalid input. Please enter a valid credit card number (12-19 digits).")


def luhn_algorithm(card_number):
    """
    Validates a credit card number using the Luhn Algorithm.
    :param card_number: The credit card number as a string
    :return: True if the card number is valid, False otherwise
    """
    total_sum = 0
    num_digits = len(card_number)
    is_even = False

    # Iterate over the digits from right to left
    for i in range(num_digits - 1, -1, -1):
        digit = int(card_number[i])
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
        is_even = not is_even

    return total_sum % 10 == 0


if __name__ == "__main__":
    print("Welcome to the Credit Card Validator! 💳")

    # Get the credit card number
    card_number = get_credit_card_number()

    # Validate the credit card number
    if luhn_algorithm(card_number):
        print(f"The credit card number '{card_number}' is valid.")
    else:
        print(f"The credit card number '{card_number}' is invalid.")