# Given two sets of numbers , Write a python program to find the missing numbers in the second
# set as compared to the first and vice versa. Use Python set

set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

missing_in_set2 = set1 - set2   
missing_in_set1 = set2 - set1   

print("Missing in second set:", missing_in_set2)
print("Missing in first set:", missing_in_set1)
