def beginning_zeros(a: str) -> int:
    import re as abc
    result = abc.split('[1-9]', a)
    return len(result[0])


# def beginning_zeros(number: str) -> int:
#     return len(number) - len(number.lstrip('0'))


# def beginning_zeros(number: str) -> int:
#     str_int = str(int(number))
#     return len(number) - len(str_int) + (str_int == '0')


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
