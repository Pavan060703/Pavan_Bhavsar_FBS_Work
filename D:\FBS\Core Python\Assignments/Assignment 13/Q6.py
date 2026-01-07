# Python Program to Multiply All the Items in a Dictionary
def mul_items(dict1):
    total=1
    for key in dict1:
        total*=dict1[key]
    return total

dict1={1:10,2:20,3:30,4:40,5:50}
result=mul_items(dict1)
print(result)