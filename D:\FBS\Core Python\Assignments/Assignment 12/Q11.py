#Python program to replace every blank space with hyphen in a string
def replaceBlank(string1):
    result=string1.replace(" ","-")
    return result

string1=input("Enter the string")
r=replaceBlank(string1)
print(r)