def count_vowels(text: str) -> int:
    """This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string.
    The function should be case-insensitive."""
    return sum(char in "aeiou" for char in text.lower())
    #     if text:
    #         return len(re.findall('[aeiou]', text.lower()))
    # text = text.lower()
    # count = 0
    # vowels = ["a", "e", "i", "o", "u"]
    # for letter in text:
    #     if letter in vowels:
    #         count += 1
    # return count


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
