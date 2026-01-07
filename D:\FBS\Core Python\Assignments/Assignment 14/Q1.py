# Write a Python Program to find elements in a given set that are not in another set. 
def difference_set(set1,set2):
    return set1.difference(set2)

set1={10,20,40,50,60}
set2={20,30,40}
result=difference_set(set1,set2)
print(result)

