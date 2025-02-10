def get_marks(prompt):
    """
    Prompts the user for marks and validates the input.
    :param prompt: The message to display to the user
    :return: A valid mark between 0 and 100
    """
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_grade(average):
    """
    Assigns a grade based on the average score.
    :param average: The average score
    :return: The corresponding grade
    """
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    print("Welcome to the Grade Calculator! 📊")

    # Get marks for five subjects
    subjects = ["Math", "Science", "English", "History", "Programming"]
    marks = []
    for subject in subjects:
        mark = get_marks(f"Enter marks for {subject} (0-100): ")
        marks.append(mark)

    # Calculate average
    total_marks = sum(marks)
    average = total_marks / len(marks)

    # Determine grade
    grade = calculate_grade(average)

    # Display the result
    print("\n--- Results ---")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")