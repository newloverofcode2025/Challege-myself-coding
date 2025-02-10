def greet(name="Guest"):
    """
    Greets a person by name. If no name is provided, defaults to 'Guest'.
    :param name: The name of the person to greet (default: 'Guest')
    """
    print(f"Hello, {name}!")


def calculate(a, b, operation="add"):
    """
    Performs a mathematical operation on two numbers.
    :param a: First number
    :param b: Second number
    :param operation: The operation to perform ('add', 'subtract', 'multiply', 'divide'; default: 'add')
    :return: The result of the operation
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


def log_message(message, level="INFO"):
    """
    Logs a message with a given log level.
    :param message: The message to log
    :param level: The log level ('INFO', 'WARNING', 'ERROR'; default: 'INFO')
    """
    print(f"[{level}] {message}")


if __name__ == "__main__":
    print("Welcome to the Default Arguments Demo! 🎯")

    # Example 1: Greet Function
    print("\nExample 1: Greet Function")
    greet()  # Uses default argument
    greet("Abhishek")  # Overrides default argument

    # Example 2: Calculator Function
    print("\nExample 2: Calculator Function")
    print("Addition:", calculate(10, 5))  # Uses default operation ('add')
    print("Subtraction:", calculate(10, 5, operation="subtract"))
    print("Multiplication:", calculate(10, 5, operation="multiply"))
    print("Division:", calculate(10, 5, operation="divide"))
    print("Invalid Operation:", calculate(10, 5, operation="mod"))

    # Example 3: Logging Function
    print("\nExample 3: Logging Function")
    log_message("This is an informational message.")  # Uses default log level ('INFO')
    log_message("This is a warning message.", level="WARNING")
    log_message("This is an error message.", level="ERROR")