import re

def get_postal_code():
    """
    Prompts the user to input a postal code.
    :return: The postal code entered by the user
    """
    return input("Enter a postal code: ").strip()

def validate_us_zip_code(postal_code):
    """
    Validates a US ZIP code (5-digit or ZIP+4 format).
    :param postal_code: The postal code to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^\d{5}(-\d{4})?$"
    return re.match(pattern, postal_code) is not None

def validate_canadian_postal_code(postal_code):
    """
    Validates a Canadian postal code (ANA NAN format).
    :param postal_code: The postal code to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$"
    return re.match(pattern, postal_code) is not None

def validate_uk_postcode(postal_code):
    """
    Validates a UK postcode.
    :param postal_code: The postal code to validate
    :return: True if valid, False otherwise
    """
    pattern = r"^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$"
    return re.match(pattern, postal_code.upper()) is not None

if __name__ == "__main__":
    print("Welcome to the Postal Code Validator! 📬")

    # Get the postal code from the user
    postal_code = get_postal_code()

    # Validate the postal code against different formats
    print("\nValidation Results:")
    print(f"US ZIP Code: {'Valid' if validate_us_zip_code(postal_code) else 'Invalid'}")
    print(f"Canadian Postal Code: {'Valid' if validate_canadian_postal_code(postal_code) else 'Invalid'}")
    print(f"UK Postcode: {'Valid' if validate_uk_postcode(postal_code) else 'Invalid'}")