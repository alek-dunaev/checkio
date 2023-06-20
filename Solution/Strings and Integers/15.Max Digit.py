def max_digit(value: int) -> int:
    mas = []
    for i in range(len(str(value))):
        mas.append(value % 10)
        value = value // 10
    return max(mas)

    # return max(map(int, str(number)))

# max_digit = lambda number: int(max(str(number)))


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

