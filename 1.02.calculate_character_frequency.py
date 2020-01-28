"""2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
RunTest = input("Run test? (y/n): ")
if RunTest == 'y':
    InputString = "google.com"
    print("Given string:", InputString)
elif RunTest == 'n':
    InputString = input("Input string: ")
else:
    InputString = RunTest

CharacterFrequency = {}
for i in InputString:
    CharacterFrequency[i] = CharacterFrequency.get(i, 0) + 1
print("Character frequency:", CharacterFrequency)
