# Athlete Sorter 🏃‍♂️🏃‍♀️

A Python script that sorts a list of athletes based on user-defined criteria such as score, age, or name.

## Features
- Represents athletes using a custom `Athlete` class with attributes like name, age, and score.
- Allows sorting by multiple criteria (e.g., score descending, name ascending).
- Displays the sorted list of athletes.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AthleteSort.git
   cd AthleteSort
   Explanation
The program works as follows:

Defines an Athlete class to represent each athlete.
Creates a list of athletes with sample data.
Prompts the user to define sorting criteria (e.g., score, name, age).
Uses Python's sorted() function with a custom key to sort the athletes.
For example:

Sorting by score descending and then by name ascending:
Alice (95) comes before Charlie (95) because "Alice" < "Charlie".
Bob (85) comes before David (85) because "Bob" < "David".