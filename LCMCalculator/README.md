# Least Common Multiple (LCM) Calculator 🔢

A Python script that calculates the least common multiple (LCM) of multiple numbers.

## Features
- Accepts multiple numbers as input from the user.
- Validates input to ensure only positive integers are accepted.
- Calculates and displays the LCM of the given numbers.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LCMCalculator.git
   cd LCMCalculator
   Explanation
The program works as follows:

Uses the math.gcd function to calculate the greatest common divisor (GCD).
Uses the relationship LCM(a, b) = |a * b| / GCD(a, b) to calculate the LCM of two numbers.
Iteratively calculates the LCM for multiple numbers.
For example, calculating the LCM of 4, 6, and 8:
LCM(4, 6) = 12
LCM(12, 8) = 24
Result: 24