class Athlete:
    """
    Represents an athlete with a name, age, and score.
    """
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"Athlete(name={self.name}, age={self.age}, score={self.score})"


def get_athletes():
    """
    Creates a list of athletes for demonstration purposes.
    :return: A list of Athlete objects
    """
    return [
        Athlete("Abhishek", 25, 95),
        Athlete("Akash", 30, 85),
        Athlete("Kritika", 22, 95),
        Athlete("David", 28, 85),
        Athlete("Eve", 27, 90)
    ]


def sort_athletes(athletes, criteria):
    """
    Sorts a list of athletes based on the given criteria.
    :param athletes: List of Athlete objects
    :param criteria: Sorting criteria as a list of tuples (attribute, reverse)
    :return: Sorted list of Athlete objects
    """
    # Use sorted() with a custom key function
    return sorted(athletes, key=lambda athlete: tuple(getattr(athlete, attr) for attr, _ in criteria), reverse=any(reverse for _, reverse in criteria))


if __name__ == "__main__":
    print("Welcome to the Athlete Sorter! 🏃‍♂️🏃‍♀️")

    # Get the list of athletes
    athletes = get_athletes()

    print("\nUnsorted Athletes:")
    for athlete in athletes:
        print(athlete)

    # Define sorting criteria
    print("\nSorting Criteria:")
    print("1. Score (Descending)")
    print("2. Name (Ascending)")
    print("3. Age (Ascending)")

    # Prompt user for sorting criteria
    criteria_input = input("Enter the sorting criteria as comma-separated numbers (e.g., '1,2'): ").strip()
    criteria_indices = [int(c.strip()) for c in criteria_input.split(",")]

    # Map indices to actual sorting criteria
    criteria_map = {
        1: ("score", True),   # Score descending
        2: ("name", False),   # Name ascending
        3: ("age", False)     # Age ascending
    }

    # Build the sorting criteria
    sorting_criteria = [criteria_map[index] for index in criteria_indices]

    # Sort the athletes
    sorted_athletes = sort_athletes(athletes, sorting_criteria)

    # Display the sorted athletes
    print("\nSorted Athletes:")
    for athlete in sorted_athletes:
        print(athlete)