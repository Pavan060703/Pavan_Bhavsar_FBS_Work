# Python program to remove the characters of Odd index values in a string.
def oddIndex(s):
    new_str=""
    for ch in s:
        new_str=s.replace((int(s.index(ch)%2!=0)),'')
    return new_str

s=input("Enter the string")
result=oddIndex(s)
print(result)