# Python Program to take in two strings and display the larger string without using built in 
# functions
def largerString(string1,string2):
    count1=0
    count2=0
    for i in string1:
        count1+=1
    for j in string2:
        count2+=1

    if count1>count2:
        return f"Larger string is {string1}"
    elif count2>count1:
        return f"Larger string is {string2}"
    else:
        return f"Both strings are equal"
    
string1=input("Enter first string")
string2=input("Enter second string")
result=largerString(string1,string2)
print(result)