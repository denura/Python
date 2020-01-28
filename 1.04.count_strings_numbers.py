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
