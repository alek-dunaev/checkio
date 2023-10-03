def count_occurrences(main_str: str, sub_str: str) -> int:
    """This function should take a main string and a substring as inputs and return the number of occurrences of the
     substring within the main string. It should not be case-sensitive and may overlap."""
    # your code here
    # return main_str.lower().count(sub_str.lower()) """ не верное на последних тестах"""
    results = 0
    sub_len = len(sub_str)
    for i in range(len(main_str)):
        if main_str[i:i + sub_len].lower() == sub_str.lower():
            results += 1
    return results


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1
assert count_occurrences('appleappleapple', 'appleapple') == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")