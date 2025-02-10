# Leap Year Checker 📅

A Python script that determines whether a given year is a leap year.

## Features
- Accepts a year as input from the user.
- Validates input to ensure only positive integers are accepted.
- Determines whether the year is a leap year based on the following rules:
  1. Divisible by 4.
  2. If divisible by 100, it must also be divisible by 400.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LeapYearChecker.git
   cd LeapYearChecker
   Explanation
The program works as follows:

Checks if the year is divisible by 4.
If the year is divisible by 100, it checks if it is also divisible by 400.
Returns True if the year satisfies the leap year conditions, otherwise returns False.
For example:

2000: Divisible by 4 and 400 → Leap year.
1900: Divisible by 4 and 100 but not by 400 → Not a leap year.
2024: Divisible by 4 but not by 100 → Leap year.