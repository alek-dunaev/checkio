

# def is_acceptable_password(password: str) -> bool:
#     return len(password) > 6 and any(i.isdigit() for i in password) and not password.isdigit()
is_acceptable_password = lambda p: 0 < sum(c.isdigit() for c in p) < len(p) > 6

print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
