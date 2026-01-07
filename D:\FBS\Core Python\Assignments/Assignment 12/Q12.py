# Python Program to count number of lowercase characters in a string.
def countLower(string1):
    count=0
    for ch in string1:
        if ch.islower():
            count+=1
    return count

string1=input("Enter the string")
result=countLower(string1)
print(result)