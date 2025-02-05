from lab import Stack

# Define matching pairs
chunk_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}

# Define syntax error values
syntax_error_values = {")": 3, "]": 57, "}": 1197, ">": 25137}

def checkForCorruption(line):
    """ Checks for corrupted chunks in a given line and returns the first illegal character found. """
    open_chunks = Stack()

    for char in line:
        if char in "([{<":
            open_chunks.push(char)
        elif char in ")]}>":
            if open_chunks.is_empty() or open_chunks.peek() != chunk_pairs[char]:
                return char  # Corrupted character found
            open_chunks.pop()

    return None  # No corruption found

# Process input file
total_syntax_score = 0

with open("3.txt", "r") as f:
    for line in f:
        corrupted_char = checkForCorruption(line.strip())
        if corrupted_char:
            total_syntax_score += syntax_error_values[corrupted_char]

print("Total Syntax Error Score:", total_syntax_score)
