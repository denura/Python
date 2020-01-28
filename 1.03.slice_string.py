"""3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given
a string. If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
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
