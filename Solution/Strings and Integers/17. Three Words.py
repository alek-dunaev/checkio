def checkio(words: str) -> bool:
    result = 0
    for i in words.split(' '):
        if i.isalpha():
            result += 1
        elif result >= 3:
            return True
        else:
            result = 0
    return result >= 3
# def checkio(words):
#     succ = 0
#     for word in words.split():
#         succ = (succ + 1)*word.isalpha()
#         if succ == 3: return True
#     else: return False

# checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())

# import re
#
# def checkio(words):
#     return True if re.search('\D+\s\D+\s\D+', words) else False

# import numpy as np
# import re
#
#
# def checkio(words: str) -> bool:
#     # find the index of words
#     # use np.diff and re to check succession
#     index_gap = np.diff([i for i, w in enumerate(words.split(' ')) if w.isalpha()])
#
#     index_str = ''.join([str(j) for j in index_gap])
#
#     pattern = re.compile(r'11')
#
#     return len(re.findall(pattern, index_str)) > 0


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
