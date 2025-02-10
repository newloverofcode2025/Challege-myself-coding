# Postal Code Validator 📬

A Python script that validates postal codes for different countries (USA, Canada, UK) using regular expressions.

## Features
- Accepts a postal code as input from the user.
- Validates the postal code against predefined formats:
  - US ZIP Code (5-digit or ZIP+4 format)
  - Canadian Postal Code (ANA NAN format)
  - UK Postcode
- Displays whether the postal code is valid for each format.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PostalCodeValidator.git
   cd PostalCodeValidator
   Explanation
The program works as follows:

Prompts the user to input a postal code.
Uses regular expressions to validate the postal code against predefined formats:
US ZIP Code: Matches 5 digits (e.g., 12345) or ZIP+4 format (e.g., 12345-6789).
Canadian Postal Code: Matches ANA NAN format (e.g., K1A 0B1).
UK Postcode: Matches UK postcode format (e.g., SW1A 1AA).
Displays whether the postal code is valid for each format.
