# Python Program to Remove the nth Index Character from a Non-Empty String
def replace(s):
    n=int(input("Enter the index to remove"))
    
    new_str=""
    for i in range(len(s)):
        if i!=n:
            new_str+=s[i]
    return new_str

s=input("Enter the string")
result=replace(s)
print(result)
