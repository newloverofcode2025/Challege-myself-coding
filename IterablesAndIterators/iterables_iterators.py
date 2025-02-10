# Example 1: Using Built-in Iterables
def explore_built_in_iterables():
    print("=== Example 1: Built-in Iterables ===")
    my_list = [1, 2, 3, 4, 5]
    my_string = "Hello"

    # Convert iterable to iterator
    list_iterator = iter(my_list)
    string_iterator = iter(my_string)

    print("List Iterator:")
    try:
        while True:
            print(next(list_iterator))
    except StopIteration:
        print("End of list iterator.\n")

    print("String Iterator:")
    try:
        while True:
            print(next(string_iterator))
    except StopIteration:
        print("End of string iterator.\n")


# Example 2: Custom Iterator
class FibonacciIterator:
    """
    A custom iterator to generate Fibonacci numbers up to a maximum value.
    """
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current


def explore_custom_iterator():
    print("=== Example 2: Custom Iterator (Fibonacci) ===")
    fibonacci_iterator = FibonacciIterator(50)
    print("Fibonacci numbers up to 50:")
    for num in fibonacci_iterator:
        print(num)
    print()


# Example 3: Using itertools
import itertools

def explore_itertools():
    print("=== Example 3: Using itertools ===")
    # Infinite iterator: itertools.count()
    print("First 5 numbers from itertools.count():")
    counter = itertools.count(start=1, step=2)
    for _ in range(5):
        print(next(counter))
    print()

    # Finite iterator: itertools.islice()
    print("First 5 Fibonacci numbers using itertools.islice():")
    fibonacci_gen = (x for x in FibonacciIterator(100))  # Generator expression
    sliced_fibonacci = itertools.islice(fibonacci_gen, 5)
    for num in sliced_fibonacci:
        print(num)
    print()


if __name__ == "__main__":
    print("Welcome to the Iterables and Iterators Demo! 🔄\n")

    # Explore built-in iterables
    explore_built_in_iterables()

    # Explore custom iterator
    explore_custom_iterator()

    # Explore itertools
    explore_itertools()