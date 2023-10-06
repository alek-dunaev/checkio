# checkio
1. This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO. If you want to know how to get the maximum out of using CheckiO, check out our blog post "From Basic to Advance usage".
This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
Input: Two arguments. Both are of type int.
2. You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.
In this mission, you need to create a password verification function.
The verification condition is:
the length should be bigger than 6.
Input: A string (str).
Output: A logic value (bool).
3. Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.
Input: An integer (int).
Output: Logic value (bool).
4. You should return a given string in reverse order.
Input: A string (str).
Output: A string (str).
5. You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").
Input: An integer (int).
Output: A string (str).
5.1 This function should take two positive numbers (length and width) as inputs and return the perimeter of a rectangle.
Input: Two integers (int).
Output: Integer (int).
6. You are given a string and you have to find its first word.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string (str).
Output: A string (str).
7. You have a non-negative integer. Try to find out how many digits it has.
Input: A non-negative integer (int).
Output: An integer (int)
8. "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
Input: An integer (int).
Output: A string (str).
8.1 This function should take a string without punctuation marks as an input and return the longest word in the string.
If there are multiple words of the same length, return the first one that appears.
Input: String (str).
Output: String (str).
8.2 This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string. 
The function should be case-insensitive.
Input: String (str).
Output: Integer (int).
9. In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit.
Input: A string (str).
Output: A logic value (bool).
10. In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string (str).
Output: A logic value (bool).
11. In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string (str).
Output: A logic value (bool).
12. In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9;
a string should not contain the word "password" in any case.
Input: A string (str).
Output: A logic value (bool).
12.1 Your function should take a string as an input and convert all the first letters of the words in the string
to uppercase, making the string a title case (other letters must be in lowercase).
Input: Original string (str).
Output: Converted string (str).
12.2 This function should take three strings as input: the main text, the target substring, and the replacement
substring. It should return a new string where all occurrences of the target substring within the main text are
replaced with the replacement substring.
Input: Three strings (str).
Output: String (str).
12.3 Given a string, find the length of the longest substring without repeating characters.
Input: String (str).
Output: Integer (int).
12.4 This function should take a non-negative integer as an input and return the factorial of that number. 
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n . 
Input: Integer (int).
Output: Integer (int).
12.5 This function should take a main string and a substring as inputs and return the number of occurrences of the 
substring within the main string. It should not be case-sensitive and may overlap.
Input: Two strings (str).
Output: Integer (int).
13. You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.
The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings (str). The second and third arguments are the initial and final markers.
Output: A string (str).
14. In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same - your function should return False.
Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first, and the third is a symbol (str) that should go after the first one.
Output: A logic value (bool).
15. You have a number and you need to determine which digit in this number is the biggest.
Input: A positive integer (int).
Output: An integer 0-9 (int). 
16. In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
Input: A string (str).
Output: An integer (int).
16.1 This function should take an list of strings and determine the longest common prefix among all the strings. If there is no common prefix, it should return an empty string.
Input: List of strings (str).
Output: String (str).
17. Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string (str) with words.
Output: Logic value (bool).
18. You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
Input: A string (str), that consists of digits.
Output: An integer (int). 
19. In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain at least 3 different (case-sensitive) letters (or digits) even if it is longer than 10
Input: A string (str).
Output: A logic value (bool).
20. For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
Input: A string (str).
Output: A string (str).
21. This function should take a date string in the format dd/mm/yyyy and convert it to the format yyyy-mm-dd.
If the input is not in the correct format, the function should return an error message "Error: Invalid date.".
Input: String (str).
Output: String (str).
22. I might see a simplified version of this mission already First Word (simplified). This mission is a little bit
more complex as not only English letters can be in the given string.
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string (str).
Output: A string (str).