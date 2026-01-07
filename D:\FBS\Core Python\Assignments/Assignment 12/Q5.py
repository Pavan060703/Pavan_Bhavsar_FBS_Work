# Python program to count the number of vowels in a string.
def countVowels(s):
    count=0
    for ch in s:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            count+=1
    return count

s=input("Enter the string")
result=countVowels(s)
print(result)