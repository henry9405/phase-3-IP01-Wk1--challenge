# phase-3-IP01-Wk1--challenge

Python code challenge

**Time Converter**
This Python script provides a simple function, convert_to_24_hour, to convert a given time from the 12-hour clock format to the 24-hour clock format. It utilizes the datetime module to achieve this conversion.

_Usage_
To use the script, simply import the convert_to_24_hour function and provide the hour, minute, and period (either "am" or "pm") as arguments. The function will return a four-digit string representing the time in the 24-hour format.

_How it Works_
The function uses the strptime method from the datetime module to create a datetime object with the given time and period. It then uses the strftime method to format the result as a four-digit string representing the time in the 24-hour format.

**Substring Value Calculator**
This Python script defines a function, solve(s), that calculates the value of the substring with the maximum sum of character values. The character values are determined by their position in the alphabet, with 'a' having a value of 1, 'b' having a value of 2, and so on.

_Usage_
To use the script, import the solve function and provide a string s as an argument. The function will return the maximum value of the consonant substrings in the input string.

**Exactly Two Positive Integers Checker**
This Python script defines a function, exactly_two_positive(a, b, c), that checks if exactly two out of three given integers are positive.

_Usage_
To use the script, import the exactly_two_positive function and provide three integers a, b, and c as arguments. The function will return True if exactly two of the three integers are positive, and False otherwise.
