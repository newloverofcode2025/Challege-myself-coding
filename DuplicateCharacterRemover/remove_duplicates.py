def remove_duplicates(input_string):
    """
    Removes duplicate characters from a string while preserving the order of first occurrences.
    :param input_string: The string to process
    :return: A string with duplicates removed
    """
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    print("Welcome to the Duplicate Character Remover! ✂️")

    # Get user input
    input_string = input("Enter a string: ").strip()

    # Remove duplicates
    result = remove_duplicates(input_string)

    # Display the result
    print(f"String after removing duplicates: {result}")