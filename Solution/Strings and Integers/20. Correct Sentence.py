def correct_sentence(text: str) -> str:
    """For the input of your function, you will be given one sentence. You have to return a corrected version,
    that starts with a capital letter and ends with a period (dot).
    Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot),
    then adding another one will be a mistake."""
    # your code here
    # text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
    # correct_sentence = lambda t: t[0].upper() + t[1:] + '.'*(t[-1] != '.')
    #     text = np.array(list(text), dtype=str)
    #     dot_at_the_end = text[-1] in '.'
    #     capital_at_start = text[0] in ascii_uppercase
    #     if not capital_at_start:
    #         text[0] = str(text[0]).upper()
    #     if not dot_at_the_end:
    #         text = np.append(text,'.')
    #     return "".join(text)
    if text.endswith("."):
        return (text[0:text.find(" ")]).title() + text[text.find(" "):]
    else:
        return (text[0:text.find(" ")]).title() + text[text.find(" "):] + "."


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print("The mission is done! Click 'Check Solution' to earn rewards!")
