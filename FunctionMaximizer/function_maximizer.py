from scipy.optimize import minimize_scalar
import numpy as np

def get_function():
    """
    Prompts the user to select a predefined function to maximize.
    :return: A callable function and its name
    """
    print("Select a function to maximize:")
    print("1. Quadratic Function: f(x) = -(x^2) + 4x + 10")
    print("2. Sine Function: f(x) = sin(x)")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        return lambda x: -(x**2) + 4*x + 10, "Quadratic Function"
    elif choice == "2":
        return lambda x: np.sin(x), "Sine Function"
    else:
        print("Invalid choice. Defaulting to Quadratic Function.")
        return lambda x: -(x**2) + 4*x + 10, "Quadratic Function"


def maximize_function(func, func_name):
    """
    Maximizes the given function using numerical optimization.
    :param func: The function to maximize
    :param func_name: Name of the function (for display purposes)
    """
    # Minimize the negative of the function to maximize it
    result = minimize_scalar(lambda x: -func(x))

    if result.success:
        max_x = result.x
        max_value = func(max_x)
        print(f"\nMaximum of {func_name}:")
        print(f"x = {max_x:.4f}")
        print(f"f(x) = {max_value:.4f}")
    else:
        print("Optimization failed.")


if __name__ == "__main__":
    print("Welcome to the Function Maximizer! 📈")

    # Get the function to maximize
    func, func_name = get_function()

    # Maximize the function
    maximize_function(func, func_name)