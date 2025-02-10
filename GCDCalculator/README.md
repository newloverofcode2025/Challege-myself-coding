# Greatest Common Divisor (GCD) Calculator 🔢

A Python script that calculates the greatest common divisor (GCD) of two numbers using both the built-in method and the Euclidean Algorithm.

## Features
- Accepts two positive integers as input from the user.
- Validates input to ensure only positive integers are accepted.
- Calculates and displays the GCD using:
  1. Python's built-in `math.gcd` function.
  2. The Euclidean Algorithm.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GCDCalculator.git
   cd GCDCalculator
   Example Usage
Input:
First Number: 56
Second Number: 98
Output:
Using Built-in Method: The GCD of 56 and 98 is: 14
Using Euclidean Algorithm: The GCD of 56 and 98 is: 14
The program works as follows:

Built-in Method : Uses Python's math.gcd function to calculate the GCD.
Euclidean Algorithm : Repeatedly replaces the larger number with the remainder of dividing the two numbers until the remainder is zero.
For example, calculating the GCD of 56 and 98:
Step 1: 98 ÷ 56 = 1 remainder 42
Step 2: 56 ÷ 42 = 1 remainder 14
Step 3: 42 ÷ 14 = 3 remainder 0
Result: 14
