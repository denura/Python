"""1. You are asked to ensure that the first and last names of people begin with a capital letter
in their passports.
For example, alison heck should be capitalized correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format:A single line of input containing the full name, S.
Constraints:* 0 < len(S) < 1000*
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized.
Example 12abc when capitalized remains 12abc.
Output Format:Print the capitalized string, S.
"""
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
    SplitFullName = FullName.split(" ")
    FinalName = ""
    for Name in SplitFullName:
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
