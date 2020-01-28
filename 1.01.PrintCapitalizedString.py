RunTest = input("Run tests? (1/2/n): ")
if RunTest == '1':
    FullName = "alison heck"
    print("Given string:", FullName)
elif RunTest == '2':
    FullName = "12abc"
    print("Given string:", FullName)
elif RunTest == 'n':
    FullName = input("What is your full name? ")
else:
    FullName = RunTest

if 0 < len(FullName) < 1000:
    SplittedFullName = FullName.split( )
    FinalName = ""
    for Name in SplittedFullName:
        if Name[0].isdigit():
            FinalName += Name + " "
        else:
            if Name.istitle():
                FinalName += Name + " "
            else:
                FinalName += Name.title() + " "
    print("Capitalized full name:", FinalName)
else:
    print('Your full name are very low or high')
