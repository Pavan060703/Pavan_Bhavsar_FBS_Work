# Python Program to sum of all items in a dictionary.
def sum_items(dict1):
    total=0
    for key in dict1:
        total+=dict1[key]
    return total

dict1={1:10,2:20,3:30,4:40,5:50}
result=sum_items(dict1)
print(result)