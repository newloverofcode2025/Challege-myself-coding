# Angle MBC Calculator 📐
Given a triangle ABC with a right angle at A, and a point M as the midpoint of side AC, we need to calculate the angle MBC. Here's how the problem can be visualized:

Triangle ABC is a right triangle with ∠CAB = 90°.
Point M is the midpoint of side AC.
We are tasked with finding the angle ∠MBC.
We'll use trigonometric principles and Python's math module to solve this problem.
Angle MBC Calculator
A Python script that calculates the angle ∠MBC based on user-provided lengths of sides AB and BC.

A Python script that calculates the angle MBC in a right triangle ABC, where:
- ∠CAB = 90°,
- M is the midpoint of side AC.

## Features
- Accepts the lengths of sides AB and BC as input from the user.
- Validates input to ensure only positive numbers are accepted.
- Ensures the triangle inequality (BC > AB) is satisfied.
- Calculates and displays the angle MBC in degrees.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AngleMBCCalculator.git
   cd AngleMBCCalculator
   Explanation
The program works as follows:

Uses the Pythagorean theorem to calculate the length of side AC.
Determines the midpoint M of side AC, so AM = MC = AC / 2.
Uses the tangent function to calculate ∠MBC:
tan(∠MBC) = MC / AB
Converts the result from radians to degrees.
For example:

AB = 3, BC = 5 → AC = √(BC² - AB²) = √(25 - 9) = 4.
MC = AC / 2 = 2.
tan(∠MBC) = MC / AB = 2 / 3 → ∠MBC ≈ 26.57°.
