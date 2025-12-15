# Python Program to Calculate the Length of a String Without Using a Library Function
def lengthString(s):
    count=0
    for i in s:
        count=count+1
    return count

s=input("Enter the string")
result=lengthString(s)
print(result)