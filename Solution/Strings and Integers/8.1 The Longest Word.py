def longest_word(sentence: str) -> str:
    """This function should take a string without punctuation marks as an input and return the longest word in the
     string. If there are multiple words of the same length, return the first one that appears."""
    # your code here
    # return sentence and sorted(reversed(sentence.split()), key=len).pop()
    text = sentence.split(' ')
    text.sort(key=len, reverse=True)
    return text[0]


print("Example:")
print(longest_word("hello world"))

# These "asserts" are used for self-checking
assert longest_word("hello world") == "hello"
assert longest_word("openai gpt-4") == "openai"
assert longest_word("this is a sentence") == "sentence"
assert longest_word("the quick brown fox") == "quick"
assert longest_word("jumped over the lazy dog") == "jumped"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
