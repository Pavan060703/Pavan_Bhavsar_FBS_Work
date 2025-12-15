#Python Program to count number of digits and letters in a string.
def countDigits(string):
    count=0
    for i in string:
        if i.isdigit():
            count+=1
    return count

string=input("Enter the string")
result=countDigits(string)
print(result)