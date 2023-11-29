def solve(s):
    # Function to calculate the value of a substring
    def substring_value(sub):
        return sum(ord(char) - ord('a') + 1 for char in sub)

    # Helper function to get all consonant substrings
    def get_consonant_substrings(s):
        consonants = "bcdfghjklmnpqrstvwxyz"
        substrings = []
        current_substring = ""

        for char in s:
            if char in consonants:
                current_substring += char
            else:
                if current_substring:
                    substrings.append(current_substring)
                current_substring = ""

        if current_substring:
            substrings.append(current_substring)

        return substrings

    # Get all consonant substrings
    consonant_substrings = get_consonant_substrings(s)

    # Calculate the value for each consonant substring and return the maximum
    max_value = max(substring_value(sub) for sub in consonant_substrings)
    
    return max_value

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
print(solve("power"))     # Output: 23
