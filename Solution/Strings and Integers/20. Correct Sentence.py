def correct_sentence(text: str) -> str:
    """For the input of your function, you will be given one sentence. You have to return a corrected version,
    that starts with a capital letter and ends with a period (dot).
    Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot),
    then adding another one will be a mistake."""
    # your code here
    return ""


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")