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
