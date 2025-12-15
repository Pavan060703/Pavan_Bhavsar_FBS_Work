# Python Program to replace all occurrences of 'a' with $ in a string
def replaceString(s):
    new_str=''
    for i in s:
        new_str=s.replace('a','$')
    return new_str

s=input("Enter the string")
result=replaceString(s)
print(result)