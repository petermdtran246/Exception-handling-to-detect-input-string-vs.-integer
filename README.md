# Exception handling to detect input string vs. integer

I. This program reads a list of single-word first names and ages (ending with "-1"), increments the age by 1, and outputs the list with the updated ages. It also handles cases where the user enters a string instead of an integer for age, preventing program crashes.

II. Features:

1. Processes a list of names and ages.
2. Increments the age by 1 for each valid entry.
3. Catches ValueError exceptions for invalid age input (strings).
4. Outputs 0 for age when encountering a string as input.
5. Terminates processing upon encountering "-1" as the name.
