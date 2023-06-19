import re


def is_acceptable_password(password: str) -> bool:
    password = password.lower()
    match = re.search("password", password)
    if not match:
        if 6 < len(password) < 9 and any(i.isdigit() for i in password) and not all(i.isdigit() for i in password):
            return True
        elif len(password) > 9:
            return True
        else:
            return False
    else:
        return False


# def is_acceptable_password(password: str) -> bool:
#     # C1 : the length should be bigger than 6;
#     # C2 : should contain at least one digit, but cannot consist of just digits.
#     # C3 : having numbers or containing just numbers does not apply to the password longer than 9.
#     # C4 : a string should not contain the word "password" in any case.
#     c1 = len(password) > 6
#     c2 = any(map(str.isdigit, password)) and not password.isdigit()
#     c3 = len(password) > 9
#     c4 = 'password' not in password.lower()
#     return c1 and (c2 or c3) and c4


print("Example:")
print(is_acceptable_password("short54"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
