def reverse_string_recursive(s):
    """
    Reverses a string using recursion.
    :param s: The string to reverse
    :return: The reversed string
    """
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: reverse the substring and append the first character at the end
    return reverse_string_recursive(s[1:]) + s[0]

if __name__ == "__main__":
    print("Welcome to the String Reverser! 🔁")

    # Get user input
    input_string = input("Enter a string to reverse: ").strip()

    # Reverse the string using recursion
    reversed_string = reverse_string_recursive(input_string)

    # Display the result
    print(f"The reversed string is: {reversed_string}")