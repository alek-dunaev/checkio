def sum_numbers(text: str) -> int:
    result = 0
    for i in text.split(' '):
        if i.isdigit():
            result += int(i)
    return result

# sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

# def sum_numbers(text: str) -> int:
#     return sum(map(int, filter(str.isdigit, text.split())))

# def sum_numbers(text: str) -> int:
#     import numpy as np
#     l = text.split(' ')
#     n = np.array([])
#     for i in l:
#         try:
#             n = np.append(n,int(i))
#         except:
#             p = 0
#     return (int(n.sum()))


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
