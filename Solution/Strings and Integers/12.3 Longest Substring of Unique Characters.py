def longest_substr(s: str) -> int:
    """Given a string, find the length of the longest substring without repeating characters."""
    # your code here
    start = res = 0
    chars = {}
    for ind, char in enumerate(s):
        if char in chars:
            start = max(start, chars[char] + 1)
        chars[char] = ind
        res = max(res, ind - start + 1)

    return res



print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
