RunTest = input("Run tests? (1/2/n): ")
if RunTest == "1":
    Set1 = [1, 2]
    Set2 = [2, 3]
    Set3 = [2]
elif RunTest == "2":
    Set1 = [1, 2]
    Set2 = [3, 4]
    Set3 = [5]
elif RunTest == "n":
    Set1 = input("Input the first set: ")
    Set2 = input("Input the second set: ")
    Set3 = input("Input the third set: ")
else:
    print("Wrong input!")
    Set1 = Set2 = Set3 = 0

if Set1:
    print("Input sets:", Set1, Set2, Set3)
    Result = "False"
    Subset = set(Set3).issubset(Set1) & set(Set3).issubset(Set2)
    if Subset:
        Result = "True"

    print("The third set is a subset of the first and the second sets:", Result)
