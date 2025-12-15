# Python program to take in a string and replace Every blank space with Hyphen.
def replaceBlank(s):
    new_str=s.replace(" ",'-')

    return new_str

s=input("Enter the string")
result=replaceBlank(s)
print(result)