"""6. Write a Python script to generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
RunTest = input("Run test? (y/n): ")
if RunTest == 'y':
    Number = 5
    print("Given number:", Number)
elif RunTest == 'n':
    Number = int(input("Input number: "))
elif RunTest.isdigit():
    Number = int(RunTest)
else:
    print("Wrong input!")
    Number = 0

if Number:
    Dictionary = {i: i ** 2 for i in range(1, Number + 1)}
    print("Result dictionary:", Dictionary)
