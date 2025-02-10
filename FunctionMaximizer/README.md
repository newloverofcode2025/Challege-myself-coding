# Function Maximizer 📈

A Python script that maximizes a given mathematical function using numerical optimization techniques.

## Features
- Allows the user to select from predefined functions (e.g., quadratic, sine).
- Uses the `scipy.optimize` library to find the maximum value of the function.
- Displays the maximum value and the corresponding input.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FunctionMaximizer.git
   cd FunctionMaximizer
   Explanation
The program works as follows:

Prompts the user to select a predefined function to maximize.
Uses the scipy.optimize.minimize_scalar function to minimize the negative of the function, effectively maximizing it.
Displays the maximum value and the corresponding input.
For example:

Quadratic Function: f(x) = -(x^2) + 4x + 10 has a maximum at x = 2, with f(x) = 14.
Sine Function: f(x) = sin(x) has a maximum at x = π/2 ≈ 1.5708, with f(x) = 1.