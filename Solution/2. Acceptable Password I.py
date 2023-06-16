def is_acceptable_password(password: str) -> bool:
    # return password.__len__() > 6
    return len(password) > 6

print("Example:")
print(is_acceptable_password("shorttter"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
