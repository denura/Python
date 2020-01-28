RunTest = input("Run tests? (1/2/3/n): ")
if RunTest == '1':
    InputString = "w3resource"
elif RunTest == '2':
    InputString = "w3"
elif RunTest == '3':
    InputString = "w"
elif RunTest == 'n':
    InputString = input("Input string: ")
else:
    InputString = RunTest

print("Given string:", InputString)
if len(InputString) < 2:
    print("Result: Empty String")
else:
    print("Result: ", InputString[:2] + InputString[-2:])
