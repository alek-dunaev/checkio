def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and not password.isdigit() and not password.isalpha()) or len(password) > 9

    # is_acceptable_password = lambda p: 0 < sum(c.isdigit() for c in p) < len(p) > 6 or len(p) > 9

    # if 6 < len(password) < 9 and any(i.isdigit() for i in password) and not all(i.isdigit() for i in password):
    #     return True
    # elif len(password) > 9:
    #     return True
    # else:
    #     return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
