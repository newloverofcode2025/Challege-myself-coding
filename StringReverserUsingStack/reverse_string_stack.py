class Stack:
    """
    A simple implementation of a stack data structure.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the stack.
        :param item: The item to push
        """
        self.items.append(item)

    def pop(self):
        """
        Pops an item from the stack.
        :return: The top item from the stack
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")

    def is_empty(self):
        """
        Checks if the stack is empty.
        :return: True if the stack is empty, False otherwise
        """
        return len(self.items) == 0

def reverse_string_using_stack(s):
    """
    Reverses a string using a stack.
    :param s: The string to reverse
    :return: The reversed string
    """
    stack = Stack()

    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)

    # Pop all characters from the stack to form the reversed string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

if __name__ == "__main__":
    print("Welcome to the String Reverser Using Stack! 🔁")

    # Get user input
    input_string = input("Enter a string to reverse: ").strip()

    # Reverse the string using a stack
    reversed_string = reverse_string_using_stack(input_string)

    # Display the result
    print(f"The reversed string is: {reversed_string}")