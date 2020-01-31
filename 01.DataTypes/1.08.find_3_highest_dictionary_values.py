"""8. Write a Python program to find the highest 3 values in a dictionary"""
from collections import Counter

SampleDictionary = {i: i ** 2 for i in range(1, 6)}
print("Sample dictionary:", SampleDictionary)

HighestValues = (Counter(SampleDictionary)).most_common(3)

print("Result dictionary with 3 highest values:", HighestValues)
