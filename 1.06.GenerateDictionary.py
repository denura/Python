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
