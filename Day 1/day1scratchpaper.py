def find_matching_combinations(words):
    combinations = []
    num_words = len(words)
    
    for i in range(num_words):
        for j in range(num_words):
            if i != j:
                # Compare last letter of words[i] with first letter of words[j]
                if words[i][-1] == words[j][0]:
                    # Add concatenated result to the list
                    combinations.append(words[i] + words[j])
    
    return combinations

# List of words
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Find matching combinations
matching_combinations = find_matching_combinations(words)

# Print the results
for combination in matching_combinations:
    print(combination)
