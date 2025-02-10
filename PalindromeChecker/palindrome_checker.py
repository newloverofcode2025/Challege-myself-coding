import string

def clean_string(s):
    """
    Removes non-alphanumeric characters and converts the string to lowercase.
    :param s: The input string
    :return: A cleaned version of the string
    """
    return ''.join(char.lower() for char in s if char.isalnum())

def is_palindrome(s):
    """
    Checks whether a string is a palindrome.
    :param s: The input string
    :return: True if the string is a palindrome, False otherwise
    """
    cleaned = clean_string(s)
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("Welcome to the Palindrome Checker! 🔁")

    # Get user input
    input_string = input("Enter a string to check if it's a palindrome: ").strip()

    # Check if the string is a palindrome
    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome!')
    else:
        print(f'"{input_string}" is not a palindrome.')