# Time Delta Calculator ⏳

A Python script that calculates the time difference (delta) between two timestamps.

## Features
- Accepts two timestamps in the format `YYYY-MM-DD HH:MM:SS`.
- Validates input to ensure correct timestamp format.
- Calculates and displays the time difference in days, hours, minutes, and seconds.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TimeDeltaCalculator.git
   cd TimeDeltaCalculator
   Explanation
The program works as follows:

Parses the input timestamps into datetime objects.
Ensures the start timestamp is earlier than the end timestamp.
Calculates the difference using Python's timedelta object.
Displays the result in days, hours, minutes, and seconds.
For example:

Start: 2023-10-01 12:00:00
End: 2023-10-02 15:30:45
Difference: 1 day, 3 hours, 30 minutes, and 45 seconds.