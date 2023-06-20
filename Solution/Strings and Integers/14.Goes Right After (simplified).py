def goes_after(word: str, first: str, second: str) -> bool:
    return word.find(first) + 1 == word.find(second)

    # try:
    #     return word.index(first) - word.index(second) == -1
    # except:
    #     return False

    # goes_after = lambda word, first, second: word.find(first) + 1 == word.find(
    #     second) if first in word and second in word else False

    # return f"{first}{second}" in word


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
