import re

# Your input string
input_string = "two1nine"

# Define a mapping from words to integers
word_to_int = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# Use regular expressions to find all words in the string
words = re.findall(r'\b\w+\b', input_string)
print(words)
# Extract and convert the word "two" if present
number = None
for word in words:
    if word in word_to_int:
        number = word_to_int[word]
        break

# Print the result
if number is not None:
    print(f"The number is: {number}")
else:
    print("No valid number word found.")