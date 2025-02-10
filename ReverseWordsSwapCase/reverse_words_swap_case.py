def reverse_words_and_swap_case(input_string):
    """
    Reverses the order of words in the input string and swaps the case of all letters.
    :param input_string: The input string containing words separated by single spaces
    :return: A string with reversed word order and swapped letter cases
    """
    # Split the string into words
    words = input_string.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Swap the case of each word and join them back into a string
    result = " ".join(word.swapcase() for word in reversed_words)
    
    return result


def get_input_string():
    """
    Prompts the user to input a string.
    :return: The input string entered by the user
    """
    return input("Enter a string of words separated by single spaces: ").strip()


if __name__ == "__main__":
    print("Welcome to the Reverse Words and Swap Case Tool! 🔀")

    # Get the input string from the user
    input_string = get_input_string()

    # Process the string
    result = reverse_words_and_swap_case(input_string)

    # Display the result
    print("\nTransformed String:")
    print(result)