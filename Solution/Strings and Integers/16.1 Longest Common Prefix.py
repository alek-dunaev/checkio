def longest_prefix(arr: list[str]) -> str:
    """This function should take an list of strings and determine the longest common prefix among all the strings.
    If there is no common prefix, it should return an empty string."""
    # arr.sort(key=len, reverse=False)
    res = ""
    # получаем пары «номер символа» — «символ» из первого слова
    for i, c in enumerate(arr[0]):
        # перебираем следующие слова в списке
        for s in arr[1:]:
            if len(s) < i + 1 or s[i] != c:
                return res
        else:
            # добавляем текущий символ к общему началу
            res += c
    # возвращаем результат
    return res


print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
