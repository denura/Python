RunTest = input("Run tests? (1/2/n): ")
if RunTest == '1':
    set1 = [1, 2]
    set2 = [2, 3]
    set3 = [2]
elif RunTest == '2':
    set1 = [1, 2]
    set2 = [3, 4]
    set3 = [5]
elif RunTest == 'n':
    set1 = input("Input the first set: ")
    set2 = input("Input the second set: ")
    set3 = input("Input the third set: ")
else:
    print("Wrong input!")
    set1 = set2 = set3 = 0

if set1:
    print("Input sets:", set1, set2, set3)
    Result = "False"
    if (set(set3).issubset(set1) & set(set3).issubset(set2)):
        Result = "True"

    print("The third set is a subset of the first and the second sets:", Result)
