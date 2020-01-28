"""4. Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
RunTest = input("Run test? (y/n): ")
if RunTest == 'y':
    InputStrings = ['abc', 'xyz', 'aba', '1221']
elif RunTest == 'n':
    InputStrings = input("Input strings (delimiter: space): ").split(" ")
else:
    InputStrings = RunTest.split(" ")

StringsCount = 0

print("Given strings:", InputStrings)

for String in InputStrings:
    if len(String) >= 2:
        if String[0] == String[-1]:
            StringsCount += 1
print("Result:", StringsCount)
