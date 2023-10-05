def between_markers(text: str, start: str, end: str) -> str:
    # check = True
    # for i in text:
    #     if i == start and check:
    #         check = False
    #         text = text.replace(i, '', 1)
    #     elif check:
    #         text = text.replace(i, '', 1)
    #     elif i == end:
    #         check = True
    #         text = text.replace(i, '', 1)
    # return text

    return text[text.index(start) + 1:text.index(end)]


# between_markers = lambda t, b, e, f=lambda x,y: x.find(y): t[f(t,b)+1:f(t,e)]

# i = text.find(begin) + 1
# j = text.find(end, i)
# return text[i:j]

print("Example:")
print(between_markers('>Apple< is simple', '>', '<'))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"
assert between_markers('>Apple< is simple', '>', '<') == 'Apple'

print("The mission is done! Click 'Check Solution' to earn rewards!")
